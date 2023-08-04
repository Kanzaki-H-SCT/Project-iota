#LICENCE :   http://www.apache.org/licenses/LICENSE-2.0
#CREATOR BY : PRANKBOT
#MOD BY ACIL
from .TProtocol import TType, TProtocolBase, TProtocolException
from struct import pack, unpack

class TBinaryProtocol(TProtocolBase):
    VERSION_MASK = -65536
    VERSION_1 = -2147418112
    TYPE_MASK = 0x000000ff
    def __init__(self, trans, strictRead=False, strictWrite=True, **kwargs):
        TProtocolBase.__init__(self, trans)
        self.strictRead = strictRead
        self.strictWrite = strictWrite
        self.string_length_limit = kwargs.get('string_length_limit', None)
        self.container_length_limit = kwargs.get('container_length_limit', None)
    def _check_string_length(self, length):
        self._check_length(self.string_length_limit, length)
    def _check_container_length(self, length):
        self._check_length(self.container_length_limit, length)
    def writeMessageBegin(self, name, type, seqid):
        if self.strictWrite:
            self.writeI32(TBinaryProtocol.VERSION_1 | type)
            self.writeString(name)
            self.writeI32(seqid)
        else:
            self.writeString(name)
            self.writeByte(type)
            self.writeI32(seqid)
    def writeMessageEnd(self):
        pass
    def writeStructBegin(self, name):
        pass
    def writeStructEnd(self):
        pass
    def writeFieldBegin(self, name, type, id):
        self.writeByte(type)
        self.writeI16(id)
    def writeFieldEnd(self):
        pass
    def writeFieldStop(self):
        self.writeByte(TType.STOP)
    def writeMapBegin(self, ktype, vtype, size):
        self.writeByte(ktype)
        self.writeByte(vtype)
        self.writeI32(size)
    def writeMapEnd(self):
        pass
    def writeListBegin(self, etype, size):
        self.writeByte(etype)
        self.writeI32(size)
    def writeListEnd(self):
        pass
    def writeSetBegin(self, etype, size):
        self.writeByte(etype)
        self.writeI32(size)
    def writeSetEnd(self):
        pass
    def writeBool(self, bool):
        if bool:
            self.writeByte(1)
        else:
            self.writeByte(0)
    def writeByte(self, byte):
        buff = pack("!b", byte)
        self.trans.write(buff)
    def writeI16(self, i16):
        buff = pack("!h", i16)
        self.trans.write(buff)
    def writeI32(self, i32):
        buff = pack("!i", i32)
        self.trans.write(buff)
    def writeI64(self, i64):
        buff = pack("!q", i64)
        self.trans.write(buff)
    def writeDouble(self, dub):
        buff = pack("!d", dub)
        self.trans.write(buff)
    def writeBinary(self, str):
        self.writeI32(len(str))
        self.trans.write(str)
    def readMessageBegin(self):
        sz = self.readI32()
        if sz < 0:
            version = sz & TBinaryProtocol.VERSION_MASK
            if version != TBinaryProtocol.VERSION_1:
                raise TProtocolException(
                    type=TProtocolException.BAD_VERSION,
                    message='Bad version in readMessageBegin: %d' % (sz))
            type = sz & TBinaryProtocol.TYPE_MASK
            name = self.readString()
            seqid = self.readI32()
        else:
            if self.strictRead:
                raise TProtocolException(type=TProtocolException.BAD_VERSION,
                                         message='No protocol version header')
            name = self.trans.readAll(sz)
            type = self.readByte()
            seqid = self.readI32()
        return (name, type, seqid)
    def readMessageEnd(self):
        pass
    def readStructBegin(self):
        pass
    def readStructEnd(self):
        pass
    def readFieldBegin(self):
        type = self.readByte()
        if type == TType.STOP:
            return (None, type, 0)
        id = self.readI16()
        return (None, type, id)
    def readFieldEnd(self):
        pass
    def readMapBegin(self):
        ktype = self.readByte()
        vtype = self.readByte()
        size = self.readI32()
        self._check_container_length(size)
        return (ktype, vtype, size)
    def readMapEnd(self):
        pass
    def readListBegin(self):
        etype = self.readByte()
        size = self.readI32()
        self._check_container_length(size)
        return (etype, size)
    def readListEnd(self):
        pass
    def readSetBegin(self):
        etype = self.readByte()
        size = self.readI32()
        self._check_container_length(size)
        return (etype, size)
    def readSetEnd(self):
        pass
    def readBool(self):
        byte = self.readByte()
        if byte == 0:
            return False
        return True
    def readByte(self):
        buff = self.trans.readAll(1)
        val, = unpack('!b', buff)
        return val
    def readI16(self):
        buff = self.trans.readAll(2)
        val, = unpack('!h', buff)
        return val
    def readI32(self):
        buff = self.trans.readAll(4)
        val, = unpack('!i', buff)
        return val
    def readI64(self):
        buff = self.trans.readAll(8)
        val, = unpack('!q', buff)
        return val
    def readDouble(self):
        buff = self.trans.readAll(8)
        val, = unpack('!d', buff)
        return val
    def readBinary(self):
        size = self.readI32()
        self._check_string_length(size)
        s = self.trans.readAll(size)
        return s
class TBinaryProtocolFactory(object):
    def __init__(self, strictRead=False, strictWrite=True, **kwargs):
        self.strictRead = strictRead
        self.strictWrite = strictWrite
        self.string_length_limit = kwargs.get('string_length_limit', None)
        self.container_length_limit = kwargs.get('container_length_limit', None)
    def getProtocol(self, trans):
        prot = TBinaryProtocol(trans, self.strictRead, self.strictWrite,
                               string_length_limit=self.string_length_limit,
                               container_length_limit=self.container_length_limit)
        return prot
class TBinaryProtocolAccelerated(TBinaryProtocol):
    pass
    def __init__(self, *args, **kwargs):
        fallback = kwargs.pop('fallback', True)
        super(TBinaryProtocolAccelerated, self).__init__(*args, **kwargs)
        try:
            from thrift.protocol import fastbinary
        except ImportError:
            if not fallback:
                raise
        else:
            self._fast_decode = fastbinary.decode_binary
            self._fast_encode = fastbinary.encode_binary
class TBinaryProtocolAcceleratedFactory(object):
    def __init__(self,
                 string_length_limit=None,
                 container_length_limit=None,
                 fallback=True):
        self.string_length_limit = string_length_limit
        self.container_length_limit = container_length_limit
        self._fallback = fallback
    def getProtocol(self, trans):
        return TBinaryProtocolAccelerated(
            trans,
            string_length_limit=self.string_length_limit,
            container_length_limit=self.container_length_limit,
            fallback=self._fallback)
#LICENCE :   http://www.apache.org/licenses/LICENSE-2.0
#CREATOR BY : PRANKBOT
#MOD BY ACIL