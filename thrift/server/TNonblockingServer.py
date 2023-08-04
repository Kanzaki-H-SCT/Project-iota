#LICENCE :   http://www.apache.org/licenses/LICENSE-2.0
#CREATOR BY : PRANKBOT
#MOD BY ACIL
import logging
import select
import socket
import struct
import threading
from collections import deque
from six.moves import queue
from thrift.transport import TTransport
from thrift.protocol.TBinaryProtocol import TBinaryProtocolFactory
__all__ = ['TNonblockingServer']
logger = logging.getLogger(__name__)
class Worker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            try:
                processor, iprot, oprot, otrans, callback = self.queue.get()
                if processor is None:
                    break
                processor.process(iprot, oprot)
                callback(True, otrans.getvalue())
            except Exception:
                logger.exception("proses...", exc_info=True)
                callback(False, b'')
WAIT_LEN = 0
WAIT_MESSAGE = 1
WAIT_PROCESS = 2
SEND_ANSWER = 3
CLOSED = 4
def locked(func):
    def nested(self, *args, **kwargs):
        self.lock.acquire()
        try:
            return func(self, *args, **kwargs)
        finally:
            self.lock.release()
    return nested
def socket_exception(func):
    def read(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except socket.error:
            logger.debug('ignoring socket exception', exc_info=True)
            self.close()
    return read
class Message(object):
    def __init__(self, offset, len_, header):
        self.offset = offset
        self.len = len_
        self.buffer = None
        self.is_header = header
    @property
    def end(self):
        return self.offset + self.len
class Connection(object):
    def __init__(self, new_socket, wake_up):
        self.socket = new_socket
        self.socket.setblocking(False)
        self.status = WAIT_LEN
        self.len = 0
        self.received = deque()
        self._reading = Message(0, 4, True)
        self._rbuf = b''
        self._wbuf = b''
        self.lock = threading.Lock()
        self.wake_up = wake_up
        self.remaining = False
    @socket_exception
    def read(self):
        assert self.status in (WAIT_LEN, WAIT_MESSAGE)
        assert not self.received
        buf_size = 8192
        first = True
        done = False
        while not done:
            read = self.socket.recv(buf_size)
            rlen = len(read)
            done = rlen < buf_size
            self._rbuf += read
            if first and rlen == 0:
                if self.status != WAIT_LEN or self._rbuf:
                    logger.error('cloud tidak terbaca')
                else:
                    logger.debug('client sudah tidak konek')
                self.close()
            while len(self._rbuf) >= self._reading.end:
                if self._reading.is_header:
                    mlen, = struct.unpack('!i', self._rbuf[:4])
                    self._reading = Message(self._reading.end, mlen, False)
                    self.status = WAIT_MESSAGE
                else:
                    self._reading.buffer = self._rbuf
                    self.received.append(self._reading)
                    self._rbuf = self._rbuf[self._reading.end:]
                    self._reading = Message(0, 4, True)
            first = False
            if self.received:
                self.status = WAIT_PROCESS
                break
        self.remaining = not done
    @socket_exception
    def write(self):
        assert self.status == SEND_ANSWER
        sent = self.socket.send(self._wbuf)
        if sent == len(self._wbuf):
            self.status = WAIT_LEN
            self._wbuf = b''
            self.len = 0
        else:
            self._wbuf = self.message[sent:]
    @locked
    def ready(self, all_ok, message):
        assert self.status == WAIT_PROCESS
        if not all_ok:
            self.close()
            self.wake_up()
            return
        self.len = 0
        if len(message) == 0:
            self._wbuf = b''
            self.status = WAIT_LEN
        else:
            self._wbuf = struct.pack('!i', len(message)) + message
            self.status = SEND_ANSWER
        self.wake_up()
    @locked
    def is_writeable(self):
        """Return True if connection should be added to write list of select"""
        return self.status == SEND_ANSWER
    @locked
    def is_readable(self):
        """Return True if connection should be added to read list of select"""
        return self.status in (WAIT_LEN, WAIT_MESSAGE)
    @locked
    def is_closed(self):
        """Returns True if connection is closed."""
        return self.status == CLOSED

    def fileno(self):
        """Returns the file descriptor of the associated socket."""
        return self.socket.fileno()
    def close(self):
        """Closes connection"""
        self.status = CLOSED
        self.socket.close()
class TNonblockingServer(object):
    """Non-blocking server."""
    def __init__(self,
                 processor,
                 lsocket,
                 inputProtocolFactory=None,
                 outputProtocolFactory=None,
                 threads=10):
        self.processor = processor
        self.socket = lsocket
        self.in_protocol = inputProtocolFactory or TBinaryProtocolFactory()
        self.out_protocol = outputProtocolFactory or self.in_protocol
        self.threads = int(threads)
        self.clients = {}
        self.tasks = queue.Queue()
        self._read, self._write = socket.socketpair()
        self.prepared = False
        self._stop = False
    def setNumThreads(self, num):
        assert not self.prepared, "Can't change number of threads after start"
        self.threads = num
    def prepare(self):
        if self.prepared:
            return
        self.socket.listen()
        for _ in range(self.threads):
            thread = Worker(self.tasks)
            thread.setDaemon(True)
            thread.start()
        self.prepared = True
    def wake_up(self):
        self._write.send(b'1')
    def stop(self):
        self._stop = True
        self.wake_up()
    def _select(self):
        readable = [self.socket.handle.fileno(), self._read.fileno()]
        writable = []
        remaining = []
        for i, connection in list(self.clients.items()):
            if connection.is_readable():
                readable.append(connection.fileno())
                if connection.remaining or connection.received:
                    remaining.append(connection.fileno())
            if connection.is_writeable():
                writable.append(connection.fileno())
            if connection.is_closed():
                del self.clients[i]
        if remaining:
            return remaining, [], [], False
        else:
            return select.select(readable, writable, readable) + (True,)

    def handle(self):
        assert self.prepared, "You have to call prepare before handle"
        rset, wset, xset, selected = self._select()
        for readable in rset:
            if readable == self._read.fileno():
                self._read.recv(1024)
            elif readable == self.socket.handle.fileno():
                try:
                    client = self.socket.accept()
                    if client:
                        self.clients[client.handle.fileno()] = Connection(client.handle,
                                                                          self.wake_up)
                except socket.error:
                    logger.debug('eror disini ', exc_info=True)
            else:
                connection = self.clients[readable]
                if selected:
                    connection.read()
                if connection.received:
                    connection.status = WAIT_PROCESS
                    msg = connection.received.popleft()
                    itransport = TTransport.TMemoryBuffer(msg.buffer, msg.offset)
                    otransport = TTransport.TMemoryBuffer()
                    iprot = self.in_protocol.getProtocol(itransport)
                    oprot = self.out_protocol.getProtocol(otransport)
                    self.tasks.put([self.processor, iprot, oprot,
                                    otransport, connection.ready])
        for writeable in wset:
            self.clients[writeable].write()
        for oob in xset:
            self.clients[oob].close()
            del self.clients[oob]
    def close(self):
        """NUTUP SERVER"""
        for _ in range(self.threads):
            self.tasks.put([None, None, None, None, None])
        self.socket.close()
        self.prepared = False
    def serve(self):
        self._stop = False
        self.prepare()
        while not self._stop:
            self.handle()
# MOD BY ACIL