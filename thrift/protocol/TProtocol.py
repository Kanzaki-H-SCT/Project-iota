#LICENCE :   http://www.apache.org/licenses/LICENSE-2.0
#CREATOR BY : PRANKBOT
#MOD BY ACIL
from thrift.unverting import TException, TType, TFrozenDict
from thrift.transport.TTransport import TTransportException
from ..compat import binary_to_str, str_to_binary
import six
import sys
from itertools import islice
from six.moves import zip
class TProtocolException(TException):
    UNKNOWN = 0
    INVALID_DATA = 1
    NEGATIVE_SIZE = 2
    SIZE_LIMIT = 3
    BAD_VERSION = 4
    NOT_IMPLEMENTED = 5
    DEPTH_LIMIT = 6
    def __init__(self, type=UNKNOWN, message=None):
        TException.__init__(self, message)
        self.type = type
class TProtocolBase(object):
    def __init__(self, trans):
        self.trans = trans
        self._fast_decode = None
        self._fast_encode = None
    @staticmethod
    def _check_length(limit, length):
        if length < 0:
            raise TTransportException(TTransportException.NEGATIVE_SIZE,
                                      'Negative length: %d' % length)
        if limit is not None and length > limit:
            raise TTransportException(TTransportException.SIZE_LIMIT,
                                      'Length exceeded max allowed: %d' % limit)
    def writeMessageBegin(self, name, ttype, seqid):
        pass
    def writeMessageEnd(self):
        pass
    def writeStructBegin(self, name):
        pass
    def writeStructEnd(self):
        pass
    def writeFieldBegin(self, name, ttype, fid):
        pass
    def writeFieldEnd(self):
        pass
    def writeFieldStop(self):
        pass
    def writeMapBegin(self, ktype, vtype, size):
        pass
    def writeMapEnd(self):
        pass
    def writeListBegin(self, etype, size):
        pass
    def writeListEnd(self):
        pass
    def writeSetBegin(self, etype, size):
        pass
    def writeSetEnd(self):
        pass
    def writeBool(self, bool_val):
        pass
    def writeByte(self, byte):
        pass
    def writeI16(self, i16):
        pass
    def writeI32(self, i32):
        pass
    def writeI64(self, i64):
        pass
    def writeDouble(self, dub):
        pass
    def writeString(self, str_val):
        self.writeBinary(str_to_binary(str_val))
    def writeBinary(self, str_val):
        pass
    def writeUtf8(self, str_val):
        self.writeString(str_val.encode('utf8'))
    def readMessageBegin(self):
        pass
    def readMessageEnd(self):
        pass
    def readStructBegin(self):
        pass
    def readStructEnd(self):
        pass
    def readFieldBegin(self):
        pass
    def readFieldEnd(self):
        pass
    def readMapBegin(self):
        pass
    def readMapEnd(self):
        pass
    def readListBegin(self):
        pass
    def readListEnd(self):
        pass
    def readSetBegin(self):
        pass
    def readSetEnd(self):
        pass
    def readBool(self):
        pass
    def readByte(self):
        pass
    def readI16(self):
        pass
    def readI32(self):
        pass
    def readI64(self):
        pass
    def readDouble(self):
        pass
    def readString(self):
        return binary_to_str(self.readBinary())
    def readBinary(self):
        pass
    def readUtf8(self):
        return self.readString().decode('utf8')
    def skip(self, ttype):
        if ttype == TType.STOP:
            return
        elif ttype == TType.BOOL:
            self.readBool()
        elif ttype == TType.BYTE:
            self.readByte()
        elif ttype == TType.I16:
            self.readI16()
        elif ttype == TType.I32:
            self.readI32()
        elif ttype == TType.I64:
            self.readI64()
        elif ttype == TType.DOUBLE:
            self.readDouble()
        elif ttype == TType.STRING:
            self.readString()
        elif ttype == TType.STRUCT:
            name = self.readStructBegin()
            while True:
                (name, ttype, id) = self.readFieldBegin()
                if ttype == TType.STOP:
                    break
                self.skip(ttype)
                self.readFieldEnd()
            self.readStructEnd()
        elif ttype == TType.MAP:
            (ktype, vtype, size) = self.readMapBegin()
            for i in range(size):
                self.skip(ktype)
                self.skip(vtype)
            self.readMapEnd()
        elif ttype == TType.SET:
            (etype, size) = self.readSetBegin()
            for i in range(size):
                self.skip(etype)
            self.readSetEnd()
        elif ttype == TType.LIST:
            (etype, size) = self.readListBegin()
            for i in range(size):
                self.skip(etype)
            self.readListEnd()
    _TTYPE_HANDLERS = (
        (None, None, False),
        (None, None, False),
        ('readBool', 'writeBool', False),
        ('readByte', 'writeByte', False),
        ('readDouble', 'writeDouble', False),
        (None, None, False),
        ('readI16', 'writeI16', False),
        (None, None, False),
        ('readI32', 'writeI32', False),
        (None, None, False),
        ('readI64', 'writeI64', False),
        ('readString', 'writeString', False),
        ('readContainerStruct', 'writeContainerStruct', True),
        ('readContainerMap', 'writeContainerMap', True),
        ('readContainerSet', 'writeContainerSet', True),
        ('readContainerList', 'writeContainerList', True),
        (None, None, False),
        (None, None, False)
    )
    def _ttype_handlers(self, ttype, spec):
        if spec == 'BINARY':
            if ttype != TType.STRING:
                raise TProtocolException(type=TProtocolException.INVALID_DATA,
                                         message='EROR DI %d' % ttype)
            return ('readBinary', 'writeBinary', False)
        if sys.version_info[0] == 2 and spec == 'UTF8':
            if ttype != TType.STRING:
                raise TProtocolException(type=TProtocolException.INVALID_DATA,
                                         message='EROR DI %d' % ttype)
            return ('readUtf8', 'writeUtf8', False)
        return self._TTYPE_HANDLERS[ttype] if ttype < len(self._TTYPE_HANDLERS) else (None, None, False)
    def _read_by_ttype(self, ttype, spec, espec):
        reader_name, _, is_container = self._ttype_handlers(ttype, espec)
        if reader_name is None:
            raise TProtocolException(type=TProtocolException.INVALID_DATA,
                                     message='EROR DI %d' % (ttype))
        reader_func = getattr(self, reader_name)
        read = (lambda: reader_func(espec)) if is_container else reader_func
        while True:
            yield read()
    def readFieldByTType(self, ttype, spec):
        return next(self._read_by_ttype(ttype, spec, spec))
    def readContainerList(self, spec):
        ttype, tspec, is_immutable = spec
        (list_type, list_len) = self.readListBegin()
        elems = islice(self._read_by_ttype(ttype, spec, tspec), list_len)
        results = (tuple if is_immutable else list)(elems)
        self.readListEnd()
        return results
    def readContainerSet(self, spec):
        ttype, tspec, is_immutable = spec
        (set_type, set_len) = self.readSetBegin()
        elems = islice(self._read_by_ttype(ttype, spec, tspec), set_len)
        results = (frozenset if is_immutable else set)(elems)
        self.readSetEnd()
        return results
    def readContainerStruct(self, spec):
        (obj_class, obj_spec) = spec
        obj = obj_class()
        obj.read(self)
        return obj
    def readContainerMap(self, spec):
        ktype, kspec, vtype, vspec, is_immutable = spec
        (map_ktype, map_vtype, map_len) = self.readMapBegin()
        keys = self._read_by_ttype(ktype, spec, kspec)
        vals = self._read_by_ttype(vtype, spec, vspec)
        keyvals = islice(zip(keys, vals), map_len)
        results = (TFrozenDict if is_immutable else dict)(keyvals)
        self.readMapEnd()
        return results
    def readStruct(self, obj, thrift_spec, is_immutable=False):
        if is_immutable:
            fields = {}
        self.readStructBegin()
        while True:
            (fname, ftype, fid) = self.readFieldBegin()
            if ftype == TType.STOP:
                break
            try:
                field = thrift_spec[fid]
            except IndexError:
                self.skip(ftype)
            else:
                if field is not None and ftype == field[1]:
                    fname = field[2]
                    fspec = field[3]
                    val = self.readFieldByTType(ftype, fspec)
                    if is_immutable:
                        fields[fname] = val
                    else:
                        setattr(obj, fname, val)
                else:
                    self.skip(ftype)
            self.readFieldEnd()
        self.readStructEnd()
        if is_immutable:
            return obj(**fields)
    def writeContainerStruct(self, val, spec):
        val.write(self)
    def writeContainerList(self, val, spec):
        ttype, tspec, _ = spec
        self.writeListBegin(ttype, len(val))
        for _ in self._write_by_ttype(ttype, val, spec, tspec):
            pass
        self.writeListEnd()
    def writeContainerSet(self, val, spec):
        ttype, tspec, _ = spec
        self.writeSetBegin(ttype, len(val))
        for _ in self._write_by_ttype(ttype, val, spec, tspec):
            pass
        self.writeSetEnd()
    def writeContainerMap(self, val, spec):
        ktype, kspec, vtype, vspec, _ = spec
        self.writeMapBegin(ktype, vtype, len(val))
        for _ in zip(self._write_by_ttype(ktype, six.iterkeys(val), spec, kspec),
                     self._write_by_ttype(vtype, six.itervalues(val), spec, vspec)):
            pass
        self.writeMapEnd()
    def writeStruct(self, obj, thrift_spec):
        self.writeStructBegin(obj.__class__.__name__)
        for field in thrift_spec:
            if field is None:
                continue
            fname = field[2]
            val = getattr(obj, fname)
            if val is None:
                continue
            fid = field[0]
            ftype = field[1]
            fspec = field[3]
            self.writeFieldBegin(fname, ftype, fid)
            self.writeFieldByTType(ftype, val, fspec)
            self.writeFieldEnd()
        self.writeFieldStop()
        self.writeStructEnd()
    def _write_by_ttype(self, ttype, vals, spec, espec):
        _, writer_name, is_container = self._ttype_handlers(ttype, espec)
        writer_func = getattr(self, writer_name)
        write = (lambda v: writer_func(v, espec)) if is_container else writer_func
        for v in vals:
            yield write(v)
    def writeFieldByTType(self, ttype, val, spec):
        next(self._write_by_ttype(ttype, [val], spec, spec))
def checkIntegerLimits(i, bits):
    if bits == 8 and (i < -128 or i > 127):
        raise TProtocolException(TProtocolException.INVALID_DATA,
                                 "i8 requires -128 <= number <= 127")
    elif bits == 16 and (i < -32768 or i > 32767):
        raise TProtocolException(TProtocolException.INVALID_DATA,
                                 "i16 requires -32768 <= number <= 32767")
    elif bits == 32 and (i < -2147483648 or i > 2147483647):
        raise TProtocolException(TProtocolException.INVALID_DATA,
                                 "i32 requires -2147483648 <= number <= 2147483647")
    elif bits == 64 and (i < -9223372036854775808 or i > 9223372036854775807):
        raise TProtocolException(TProtocolException.INVALID_DATA,
                                 "i64 requires -9223372036854775808 <= number <= 9223372036854775807")
class TProtocolFactory(object):
    def getProtocol(self, trans):
        pass
