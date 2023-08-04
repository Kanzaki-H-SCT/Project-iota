# INI NYAMBUNG KE FROZEN
# ACIL. MOD

import sys
class TType(object):
    STOP = 0
    VOID = 1
    BOOL = 2
    BYTE = 3
    I08 = 3
    DOUBLE = 4
    I16 = 6
    I32 = 8
    I64 = 10
    STRING = 11
    UTF7 = 11
    STRUCT = 12
    MAP = 13
    SET = 14
    LIST = 15
    UTF8 = 16
    UTF16 = 17
    _VALUES_TO_NAMES = (
        'STOP',
        'VOID',
        'BOOL',
        'BYTE',
        'DOUBLE',
        None,
        'I16',
        None,
        'I32',
        None,
        'I64',
        'STRING',
        'STRUCT',
        'MAP',
        'SET',
        'LIST',
        'UTF8',
        'UTF16',
    )
class TMessageType(object):
    CALL = 1
    REPLY = 2
    EXCEPTION = 3
    ONEWAY = 4
class PrankbotProses(object):
    """ini prosesor nya"""

    def process(self, iprot, oprot):
        pass
class TException(Exception):
    """ini Exception sob"""
    # INI SUPORT DI PYTHON2 ATAU PYTHON3
    if (2, 6, 0) <= sys.version_info < (3, 0):
        def _get_message(self):
            return self._message
        def _set_message(self, message):
            self._message = message
        message = property(_get_message, _set_message)
    def __init__(self, message=None):
        Exception.__init__(self, message)
        self.message = message
class TApplicationException(TException):
    """INI LEVEL THRIFT NYA SOB"""
    UNKNOWN = 0
    UNKNOWN_METHOD = 1
    INVALID_MESSAGE_TYPE = 2
    WRONG_METHOD_NAME = 3
    BAD_SEQUENCE_ID = 4
    MISSING_RESULT = 5
    INTERNAL_ERROR = 6
    PROTOCOL_ERROR = 7
    INVALID_TRANSFORM = 8
    INVALID_PROTOCOL = 9
    UNSUPPORTED_CLIENT_TYPE = 10
    def __init__(self, type=UNKNOWN, message=None):
        TException.__init__(self, message)
        self.type = type
    def __str__(self):
        if self.message:
            return self.message
        elif self.type == self.UNKNOWN_METHOD:
            return 'TIDAK ADA METODE [0]'
        elif self.type == self.INVALID_MESSAGE_TYPE:
            return 'TIDAK ADA PESAN [0]'
        elif self.type == self.WRONG_METHOD_NAME:
            return 'NAMA TIDAK VALID'
        elif self.type == self.BAD_SEQUENCE_ID:
            return 'SQUENCE TIDAK SUPORT'
        elif self.type == self.MISSING_RESULT:
            return 'RESPON DI TAMPILKAN'
        elif self.type == self.INTERNAL_ERROR:
            return 'RUANG EROR'
        elif self.type == self.PROTOCOL_ERROR:
            return 'PROTOCOL EROR'
        elif self.type == self.INVALID_TRANSFORM:
            return 'TRANSFORM'
        elif self.type == self.INVALID_PROTOCOL:
            return 'INVALID PRO'
        elif self.type == self.UNSUPPORTED_CLIENT_TYPE:
            return 'CLIENT TIDAK SUPORT INI'
        else:
            return 'JANGAN SOMBONG DENGAN APA YANG KAU BISA. SEMUA MILIK ALLAH SWT'
    # MEMBACA LIBS
    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.message = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
    def write(self, oprot):
        oprot.writeStructBegin('TApplicationException')
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 1)
            oprot.writeString(self.message)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
class TFrozenDict(dict):
    """PROZENDICT"""
    def __init__(self, *args, **kwargs):
        super(TFrozenDict, self).__init__(*args, **kwargs)
        # INI UNTUK MENGETAHUI DIMANA SC LU EROR DAN UNTUK MENSTOP RUN BOT LU
        self.__hashval = hash(TFrozenDict) ^ hash(tuple(sorted(self.items())))
    def __setitem__(self, *args):
        raise TypeError("MODIF BY PRANKBOT")
    def __delitem__(self, *args):
        raise TypeError("MODIF BY PRANKBOT")
    def __hash__(self):
        return self.__hashval
# SEKIAN DAN TRIMAKASIH.