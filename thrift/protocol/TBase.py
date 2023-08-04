#LICENCE :   http://www.apache.org/licenses/LICENSE-2.0
#CREATOR BY : PRANKBOT
#MOD BY ACIL
from thrift.transport import TTransport
class TBase(object):
    __slots__ = ()
    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key)) for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True
    def __ne__(self, other):
        return not (self == other)
    def read(self, iprot):
        if (iprot._fast_decode is not None and
                isinstance(iprot.trans, TTransport.CReadableTransport) and
                self.thrift_spec is not None):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
        else:
            iprot.readStruct(self, self.thrift_spec)
    def write(self, oprot):
        if (oprot._fast_encode is not None and self.thrift_spec is not None):
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
        else:
            oprot.writeStruct(self, self.thrift_spec)
class TExceptionBase(TBase, Exception):
    pass
class TFrozenBase(TBase):
    def __setitem__(self, *args):
        raise TypeError("MODIF BY PRANKBOTS")
    def __delitem__(self, *args):
        raise TypeError("MODIF BY PRANKBOTS")
    def __hash__(self, *args):
        return hash(self.__class__) ^ hash(self.__slots__)
    @classmethod
    def read(cls, iprot):
        if (iprot._fast_decode is not None and
                isinstance(iprot.trans, TTransport.CReadableTransport) and
                cls.thrift_spec is not None):
            self = cls()
            return iprot._fast_decode(None, iprot,
                                      [self.__class__, self.thrift_spec])
        else:
            return iprot.readStruct(cls, cls.thrift_spec, True)
#LICENCE :   http://www.apache.org/licenses/LICENSE-2.0
#CREATOR BY : PRANKBOT
#MOD BY ACIL