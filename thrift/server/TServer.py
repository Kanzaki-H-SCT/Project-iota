#LICENCE :   http://www.apache.org/licenses/LICENSE-2.0
#CREATOR BY : PRANKBOT
#MOD BY ACIL
from six.moves import queue
import logging
import os
import threading
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
logger = logging.getLogger(__name__)
class TServer(object):
    def __init__(self, *args):
        if (len(args) == 2):
            self.__initArgs__(args[0], args[1],
                              TTransport.TTransportFactoryBase(),
                              TTransport.TTransportFactoryBase(),
                              TBinaryProtocol.TBinaryProtocolFactory(),
                              TBinaryProtocol.TBinaryProtocolFactory())
        elif (len(args) == 4):
            self.__initArgs__(args[0], args[1], args[2], args[2], args[3], args[3])
        elif (len(args) == 6):
            self.__initArgs__(args[0], args[1], args[2], args[3], args[4], args[5])
    def __initArgs__(self, processor, serverTransport,
                     inputTransportFactory, outputTransportFactory,
                     inputProtocolFactory, outputProtocolFactory):
        self.processor = processor
        self.serverTransport = serverTransport
        self.inputTransportFactory = inputTransportFactory
        self.outputTransportFactory = outputTransportFactory
        self.inputProtocolFactory = inputProtocolFactory
        self.outputProtocolFactory = outputProtocolFactory
    def serve(self):
        pass
class TSimpleServer(TServer):
    def __init__(self, *args):
        TServer.__init__(self, *args)
    def serve(self):
        self.serverTransport.listen()
        while True:
            client = self.serverTransport.accept()
            if not client:
                continue
            itrans = self.inputTransportFactory.getTransport(client)
            otrans = self.outputTransportFactory.getTransport(client)
            iprot = self.inputProtocolFactory.getProtocol(itrans)
            oprot = self.outputProtocolFactory.getProtocol(otrans)
            try:
                while True:
                    self.processor.process(iprot, oprot)
            except TTransport.TTransportException:
                pass
            except Exception as x:
                logger.exception(x)
            itrans.close()
            otrans.close()
class TThreadedServer(TServer):
    def __init__(self, *args, **kwargs):
        TServer.__init__(self, *args)
        self.daemon = kwargs.get("daemon", False)
    def serve(self):
        self.serverTransport.listen()
        while True:
            try:
                client = self.serverTransport.accept()
                if not client:
                    continue
                t = threading.Thread(target=self.handle, args=(client,))
                t.setDaemon(self.daemon)
                t.start()
            except KeyboardInterrupt:
                raise
            except Exception as x:
                logger.exception(x)
    def handle(self, client):
        itrans = self.inputTransportFactory.getTransport(client)
        otrans = self.outputTransportFactory.getTransport(client)
        iprot = self.inputProtocolFactory.getProtocol(itrans)
        oprot = self.outputProtocolFactory.getProtocol(otrans)
        try:
            while True:
                self.processor.process(iprot, oprot)
        except TTransport.TTransportException:
            pass
        except Exception as x:
            logger.exception(x)
        itrans.close()
        otrans.close()
class TThreadPoolServer(TServer):
    def __init__(self, *args, **kwargs):
        TServer.__init__(self, *args)
        self.clients = queue.Queue()
        self.threads = 10
        self.daemon = kwargs.get("daemon", False)
    def setNumThreads(self, num):
        self.threads = num
    def serveThread(self):
        while True:
            try:
                client = self.clients.get()
                self.serveClient(client)
            except Exception as x:
                logger.exception(x)

    def serveClient(self, client):
        itrans = self.inputTransportFactory.getTransport(client)
        otrans = self.outputTransportFactory.getTransport(client)
        iprot = self.inputProtocolFactory.getProtocol(itrans)
        oprot = self.outputProtocolFactory.getProtocol(otrans)
        try:
            while True:
                self.processor.process(iprot, oprot)
        except TTransport.TTransportException:
            pass
        except Exception as x:
            logger.exception(x)
        itrans.close()
        otrans.close()
    def serve(self):
        for i in range(self.threads):
            try:
                t = threading.Thread(target=self.serveThread)
                t.setDaemon(self.daemon)
                t.start()
            except Exception as x:
                logger.exception(x)
        self.serverTransport.listen()
        while True:
            try:
                client = self.serverTransport.accept()
                if not client:
                    continue
                self.clients.put(client)
            except Exception as x:
                logger.exception(x)
class TForkingServer(TServer):
    def __init__(self, *args):
        TServer.__init__(self, *args)
        self.children = []
    def serve(self):
        def try_close(file):
            try:
                file.close()
            except IOError as e:
                logger.warning(e, exc_info=True)
        self.serverTransport.listen()
        while True:
            client = self.serverTransport.accept()
            if not client:
                continue
            try:
                pid = os.fork()
                if pid:
                    self.children.append(pid)
                    self.collect_children()
                    itrans = self.inputTransportFactory.getTransport(client)
                    otrans = self.outputTransportFactory.getTransport(client)
                    try_close(itrans)
                    try_close(otrans)
                else:
                    itrans = self.inputTransportFactory.getTransport(client)
                    otrans = self.outputTransportFactory.getTransport(client)
                    iprot = self.inputProtocolFactory.getProtocol(itrans)
                    oprot = self.outputProtocolFactory.getProtocol(otrans)
                    ecode = 0
                    try:
                        try:
                            while True:
                                self.processor.process(iprot, oprot)
                        except TTransport.TTransportException:
                            pass
                        except Exception as e:
                            logger.exception(e)
                            ecode = 1
                    finally:
                        try_close(itrans)
                        try_close(otrans)
                    os._exit(ecode)
            except TTransport.TTransportException:
                pass
            except Exception as x:
                logger.exception(x)
    def collect_children(self):
        while self.children:
            try:
                pid, status = os.waitpid(0, os.WNOHANG)
            except os.error:
                pid = None

            if pid:
                self.children.remove(pid)
            else:
                break
# MOD BY ACIL
# CREATOR BY PRANKBOTS