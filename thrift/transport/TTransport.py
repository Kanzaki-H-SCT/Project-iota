#LICENCE :   http://www.apache.org/licenses/LICENSE-2.0
#CREATOR BY : PRANKBOT
#MOD BY ACIL
from struct import pack, unpack
from thrift.unverting import TException
from ..compat import BufferIO
class TTransportException(TException):
    UNKNOWN = 0
    NOT_OPEN = 1
    ALREADY_OPEN = 2
    TIMED_OUT = 3
    END_OF_FILE = 4
    NEGATIVE_SIZE = 5
    SIZE_LIMIT = 6
    def __init__(self, type=UNKNOWN, message=None):
        TException.__init__(self, message)
        self.type = type
class TTransportBase(object):
    def isOpen(self):
        pass
    def open(self):
        pass
    def close(self):
        pass
    def read(self, sz):
        pass
    def readAll(self, sz):
        buff = b''
        have = 0
        while (have < sz):
            chunk = self.read(sz - have)
            chunkLen = len(chunk)
            have += chunkLen
            buff += chunk
            if chunkLen == 0:
                raise EOFError()
        return buff
    def write(self, buf):
        pass
    def flush(self):
        pass
class CReadableTransport(object):
    @property
    def cstringio_buf(self):
        pass
    def cstringio_refill(self, partialread, reqlen):
        pass
class TServerTransportBase(object):
    def listen(self):
        pass
    def accept(self):
        pass
    def close(self):
        pass
class TTransportFactoryBase(object):
    def getTransport(self, trans):
        return trans
class TBufferedTransportFactory(object):
    def getTransport(self, trans):
        buffered = TBufferedTransport(trans)
        return buffered
class TBufferedTransport(TTransportBase, CReadableTransport):
    DEFAULT_BUFFER = 4096
    def __init__(self, trans, rbuf_size=DEFAULT_BUFFER):
        self.__trans = trans
        self.__wbuf = BufferIO()
        self.__rbuf = BufferIO(b'')
        self.__rbuf_size = rbuf_size
    def isOpen(self):
        return self.__trans.isOpen()
    def open(self):
        return self.__trans.open()
    def close(self):
        return self.__trans.close()
    def read(self, sz):
        ret = self.__rbuf.read(sz)
        if len(ret) != 0:
            return ret
        self.__rbuf = BufferIO(self.__trans.read(max(sz, self.__rbuf_size)))
        return self.__rbuf.read(sz)

    def write(self, buf):
        try:
            self.__wbuf.write(buf)
        except Exception as e:
            self.__wbuf = BufferIO()
            raise e
    def flush(self):
        out = self.__wbuf.getvalue()
        self.__wbuf = BufferIO()
        self.__trans.write(out)
        self.__trans.flush()
    @property
    def cstringio_buf(self):
        return self.__rbuf
    def cstringio_refill(self, partialread, reqlen):
        retstring = partialread
        if reqlen < self.__rbuf_size:
            retstring += self.__trans.read(self.__rbuf_size)
        if len(retstring) < reqlen:
            retstring += self.__trans.readAll(reqlen - len(retstring))
        self.__rbuf = BufferIO(retstring)
        return self.__rbuf
class TMemoryBuffer(TTransportBase, CReadableTransport):
    def __init__(self, value=None, offset=0):
        if value is not None:
            self._buffer = BufferIO(value)
        else:
            self._buffer = BufferIO()
        if offset:
            self._buffer.seek(offset)
    def isOpen(self):
        return not self._buffer.closed
    def open(self):
        pass
    def close(self):
        self._buffer.close()
    def read(self, sz):
        return self._buffer.read(sz)
    def write(self, buf):
        self._buffer.write(buf)
    def flush(self):
        pass
    def getvalue(self):
        return self._buffer.getvalue()
    @property
    def cstringio_buf(self):
        return self._buffer
    def cstringio_refill(self, partialread, reqlen):
        raise EOFError()
class TFramedTransportFactory(object):
    def getTransport(self, trans):
        framed = TFramedTransport(trans)
        return framed
class TFramedTransport(TTransportBase, CReadableTransport):
    def __init__(self, trans,):
        self.__trans = trans
        self.__rbuf = BufferIO(b'')
        self.__wbuf = BufferIO()
    def isOpen(self):
        return self.__trans.isOpen()
    def open(self):
        return self.__trans.open()
    def close(self):
        return self.__trans.close()
    def read(self, sz):
        ret = self.__rbuf.read(sz)
        if len(ret) != 0:
            return ret
        self.readFrame()
        return self.__rbuf.read(sz)
    def readFrame(self):
        buff = self.__trans.readAll(4)
        sz, = unpack('!i', buff)
        self.__rbuf = BufferIO(self.__trans.readAll(sz))
    def write(self, buf):
        self.__wbuf.write(buf)
    def flush(self):
        wout = self.__wbuf.getvalue()
        wsz = len(wout)
        self.__wbuf = BufferIO()
        buf = pack("!i", wsz) + wout
        self.__trans.write(buf)
        self.__trans.flush()
    @property
    def cstringio_buf(self):
        return self.__rbuf
    def cstringio_refill(self, prefix, reqlen):
        while len(prefix) < reqlen:
            self.readFrame()
            prefix += self.__rbuf.getvalue()
        self.__rbuf = BufferIO(prefix)
        return self.__rbuf
class TFileObjectTransport(TTransportBase):
    def __init__(self, fileobj):
        self.fileobj = fileobj
    def isOpen(self):
        return True
    def close(self):
        self.fileobj.close()
    def read(self, sz):
        return self.fileobj.read(sz)
    def write(self, buf):
        self.fileobj.write(buf)
    def flush(self):
        self.fileobj.flush()
class TSaslClientTransport(TTransportBase, CReadableTransport):
    START = 1
    OK = 2
    BAD = 3
    ERROR = 4
    COMPLETE = 5
    def __init__(self, transport, host, service, mechanism='GSSAPI',
                 **sasl_kwargs):
        from puresasl.client import SASLClient
        self.transport = transport
        self.sasl = SASLClient(host, service, mechanism, **sasl_kwargs)
        self.__wbuf = BufferIO()
        self.__rbuf = BufferIO(b'')
    def open(self):
        if not self.transport.isOpen():
            self.transport.open()
        self.send_sasl_msg(self.START, self.sasl.mechanism)
        self.send_sasl_msg(self.OK, self.sasl.process())
        while True:
            status, challenge = self.recv_sasl_msg()
            if status == self.OK:
                self.send_sasl_msg(self.OK, self.sasl.process(challenge))
            elif status == self.COMPLETE:
                if not self.sasl.complete:
                    raise TTransportException(
                        TTransportException.NOT_OPEN,
                        "importing server.. this "
                        "sudah dilakukan")
                else:
                    break
            else:
                raise TTransportException(
                    TTransportException.NOT_OPEN,
                    "statistik: %d (%s)"
                    % (status, challenge))
    def send_sasl_msg(self, status, body):
        header = pack(">BI", status, len(body))
        self.transport.write(header + body)
        self.transport.flush()
    def recv_sasl_msg(self):
        header = self.transport.readAll(5)
        status, length = unpack(">BI", header)
        if length > 0:
            payload = self.transport.readAll(length)
        else:
            payload = ""
        return status, payload
    def write(self, data):
        self.__wbuf.write(data)
    def flush(self):
        data = self.__wbuf.getvalue()
        encoded = self.sasl.wrap(data)
        self.transport.write(''.join((pack("!i", len(encoded)), encoded)))
        self.transport.flush()
        self.__wbuf = BufferIO()
    def read(self, sz):
        ret = self.__rbuf.read(sz)
        if len(ret) != 0:
            return ret
        self._read_frame()
        return self.__rbuf.read(sz)
    def _read_frame(self):
        header = self.transport.readAll(4)
        length, = unpack('!i', header)
        encoded = self.transport.readAll(length)
        self.__rbuf = BufferIO(self.sasl.unwrap(encoded))
    def close(self):
        self.sasl.dispose()
        self.transport.close()
    @property
    def cstringio_buf(self):
        return self.__rbuf
    def cstringio_refill(self, prefix, reqlen):
        while len(prefix) < reqlen:
            self._read_frame()
            prefix += self.__rbuf.getvalue()
        self.__rbuf = BufferIO(prefix)
        return self.__rbuf
# CREATED BY ACIL MODIF.