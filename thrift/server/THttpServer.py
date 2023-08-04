#LICENCE :   http://www.apache.org/licenses/LICENSE-2.0
#CREATOR BY : PRANKBOT
#MOD BY ACIL
from six.moves import BaseHTTPServer
from thrift.server import TServer
from thrift.transport import TTransport
class ResponseException(Exception):
    def __init__(self, handler):
        self.handler = handler
class THttpServer(TServer.TServer):
    def __init__(self,
                 processor,
                 server_address,
                 inputProtocolFactory,
                 outputProtocolFactory=None,
                 server_class=BaseHTTPServer.HTTPServer):
        if outputProtocolFactory is None:
            outputProtocolFactory = inputProtocolFactory
        TServer.TServer.__init__(self, processor, None, None, None,
                                 inputProtocolFactory, outputProtocolFactory)
        thttpserver = self
        class RequestHander(BaseHTTPServer.BaseHTTPRequestHandler):
            def do_POST(self):
                itrans = TTransport.TFileObjectTransport(self.rfile)
                otrans = TTransport.TFileObjectTransport(self.wfile)
                itrans = TTransport.TBufferedTransport(
                    itrans, int(self.headers['Content-Length']))
                otrans = TTransport.TMemoryBuffer()
                iprot = thttpserver.inputProtocolFactory.getProtocol(itrans)
                oprot = thttpserver.outputProtocolFactory.getProtocol(otrans)
                try:
                    thttpserver.processor.process(iprot, oprot)
                except ResponseException as exn:
                    exn.handler(self)
                else:
                    self.send_response(200)
                    self.send_header("content-type", "application/x-thrift")
                    self.end_headers()
                    self.wfile.write(otrans.getvalue())
        self.httpd = server_class(server_address, RequestHander)
    def serve(self):
        self.httpd.serve_forever()
# MOD BY ACIL