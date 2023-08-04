#LICENCE :   http://www.apache.org/licenses/LICENSE-2.0
#CREATOR BY : PRANKBOT
#MOD BY ACIL
from __future__ import division
import zlib
from .TTransport import TTransportBase, CReadableTransport
from ..compat import BufferIO
class TZlibTransportFactory(object):
    # proses cache ke Zlibs
    _last_trans = None
    _last_z = None
    def getTransport(self, trans, compresslevel=9):
        if trans == self._last_trans:
            return self._last_z
        ztrans = TZlibTransport(trans, compresslevel)
        self._last_trans = trans
        self._last_z = ztrans
        return ztrans
class TZlibTransport(TTransportBase, CReadableTransport):
    DEFAULT_BUFFSIZE = 4096
    def __init__(self, trans, compresslevel=9):
        self.__trans = trans
        self.compresslevel = compresslevel
        self.__rbuf = BufferIO()
        self.__wbuf = BufferIO()
        self._init_zlib()
        self._init_stats()
    def _reinit_buffers(self):
        self.__rbuf = BufferIO()
        self.__wbuf = BufferIO()
    def _init_stats(self):
        self.bytes_in = 0
        self.bytes_out = 0
        self.bytes_in_comp = 0
        self.bytes_out_comp = 0
    def _init_zlib(self):
        self._zcomp_read = zlib.decompressobj()
        self._zcomp_write = zlib.compressobj(self.compresslevel)
    def getCompRatio(self):
        r_percent, w_percent = (None, None)
        if self.bytes_in > 0:
            r_percent = self.bytes_in_comp / self.bytes_in
        if self.bytes_out > 0:
            w_percent = self.bytes_out_comp / self.bytes_out
        return (r_percent, w_percent)
    def getCompSavings(self):
        r_saved = self.bytes_in - self.bytes_in_comp
        w_saved = self.bytes_out - self.bytes_out_comp
        return (r_saved, w_saved)
    def isOpen(self):
        #transport open
        return self.__trans.isOpen()
    def open(self):
        # ini jalurnya
        self._init_stats()
        return self.__trans.open()
    def listen(self):
        self.__trans.listen()
    def accept(self):
        # menerima transport
        return self.__trans.accept()
    def close(self):
        #penutupan transport
        self._reinit_buffers()
        self._init_zlib()
        return self.__trans.close()
    def read(self, sz):
        ret = self.__rbuf.read(sz)
        if len(ret) > 0:
            return ret
        # kembali reaksi transport
        while True:
            if self.readComp(sz):
                break
        ret = self.__rbuf.read(sz)
        return ret
    def readComp(self, sz):
        zbuf = self.__trans.read(sz)
        zbuf = self._zcomp_read.unconsumed_tail + zbuf
        buf = self._zcomp_read.decompress(zbuf)
        self.bytes_in += len(zbuf)
        self.bytes_in_comp += len(buf)
        old = self.__rbuf.read()
        self.__rbuf = BufferIO(old + buf)
        if len(old) + len(buf) == 0:
            return False
        return True
    def write(self, buf):
        self.__wbuf.write(buf)
    def flush(self):
        wout = self.__wbuf.getvalue()
        if len(wout) > 0:
            zbuf = self._zcomp_write.compress(wout)
            self.bytes_out += len(wout)
            self.bytes_out_comp += len(zbuf)
        else:
            zbuf = ''
        ztail = self._zcomp_write.flush(zlib.Z_SYNC_FLUSH)
        self.bytes_out_comp += len(ztail)
        if (len(zbuf) + len(ztail)) > 0:
            self.__wbuf = BufferIO()
            self.__trans.write(zbuf + ztail)
        self.__trans.flush()
    @property
    def cstringio_buf(self):
        return self.__rbuf
    def cstringio_refill(self, partialread, reqlen):
        retstring = partialread
        if reqlen < self.DEFAULT_BUFFSIZE:
            retstring += self.read(self.DEFAULT_BUFFSIZE)
        while len(retstring) < reqlen:
            retstring += self.read(reqlen - len(retstring))
        self.__rbuf = BufferIO(retstring)
        return self.__rbuf
# JANGAN SOMBONG APA YANG KAMU PUNYA DAN APA YANG KAMU BISA
# SEMUA MILIK ALLAH SWT