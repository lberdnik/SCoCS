from src.constants import DEFAULT_PRIMITIVE_TYPES, UNSERIALIZERABLE_TYPES \
    #

class Encoder:
    
    @classmethod
    def encode(cls, obj):
        if isinstance(obj, DEFAULT_PRIMITIVE_TYPES):
            return obj
    
    @classmethod
    def decode(cls, obj):
        if isinstance(obj, DEFAULT_PRIMITIVE_TYPES):
            return obj
    
    @classmethod
    def _encode_collection(cls, obj):
        pass

    @classmethod
    def _encode_function(cls, obj):
        pass

    @classmethod
    def _encode_class(cls, obj):
        pass

    @classmethod
    def _encode_object(cls, obj):
        pass

    @classmethod
    def _encode_module(cls, obj):
        pass
    
    @classmethod
    def _encode_cell(cls, obj):     #
        pass

    @classmethod
    def _encode_code(cls, obj):     #
        pass

    @classmethod
    def _encode_iterator(cls, obj): #
        pass

    @classmethod
    def _encode_bytes(cls, obj: bytes): #
        pass
    
    @classmethod
    def _decode_collection(cls, obj):
        pass

    @classmethod
    def _decode_function(cls, obj):
        pass

    @classmethod
    def _decode_class(cls, obj):
        pass

    @classmethod
    def _decode_object(cls, obj):
        pass

    @classmethod
    def _decode_module(cls, obj):
        pass
    
    @classmethod
    def _decode_cell(cls, obj):     #
        pass

    @classmethod
    def _decode_code(cls, obj):     #
        pass

    @classmethod
    def _decode_iterator(cls, obj): #
        pass

    @classmethod
    def _decode_bytes(cls, obj: bytes): #
        pass    