import base64
import builtins
import inspect
import math 
import src.complement

from src.constants import DEFAULT_PRIMITIVE_TYPES, UNSERIALIZERABLE_TYPES, \
    UNSERIALIZERABLE_TYPES, UNSERIALIZERABLE_TYPES, \
    ITERATOR_TYPE, CODE_TYPE, CELL_TYPE, MODULE_TYPE, FUNCTION_TYPE, \
    BYTES_TYPE, CLASS_TYPE, OBJ_TYPE, TUPLE_TYPE, SET_TYPE

from types import ModuleType, CellType, FunctionType, MethodType, CodeType

class Encoder:
    
    @classmethod
    def encode(cls, obj):
        if isinstance(obj, DEFAULT_PRIMITIVE_TYPES):
            return obj
        if isinstance(obj, ModuleType):
            return cls._encode_module(obj)
        if isinstance(obj, CellType):
            return cls._encode_cell(obj)
        if isinstance(obj, bytes):
            return cls._encode_bytes(obj)
        if isinstance(obj, list):
            return type(obj)((cls.convert(item) for item in obj)) 
        if isinstance(obj, (tuple, set)):
            return cls._encode_collection(obj)
        if isinstance(obj, dict):
            return {key: cls.convert(value) for key, value in obj.items()}
        if isinstance(obj, (FunctionType, MethodType)):
            return cls._encode_function(obj)
        if isinstance(obj, type):          
            return cls._encode_class(obj)
        if cls.is_iterable(obj):
            return cls._encode_iterator(obj)
        if isinstance(obj, CodeType):
            return cls._encode_code(obj)
        if isinstance(obj, object):
            return cls._encode_object(obj)
    
    @classmethod
    def decode(cls, obj):
        if isinstance(obj, DEFAULT_PRIMITIVE_TYPES):
            return obj
        if isinstance(obj, list):
            return type(obj)((cls.deconvert(item) for item in obj))
        if isinstance(obj, dict):
            type_to_decode = cls._get_type(obj) 

            if type_to_decode is None:          
                return {key: cls.deconvert(value) for key, value in obj.items()}
            if type_to_decode == BYTES_TYPE:
                return cls._decode_bytes(obj)
            if type_to_decode == FUNCTION_TYPE:
                return cls._decode_function(obj)
            if type_to_decode == CELL_TYPE:
                return cls._decode_cell(obj)
            if type_to_decode == CLASS_TYPE:
                return cls._decode_class(obj)
            if type_to_decode == ITERATOR_TYPE:
                return cls._decode_iterator(obj)
            if type_to_decode == CODE_TYPE:
                return cls._decode_code(obj)
            if type_to_decode == MODULE_TYPE:
                return cls._decode_module(obj)
            if type_to_decode in (TUPLE_TYPE, SET_TYPE):
                return cls._decode_collection(obj)
            if type_to_decode == OBJ_TYPE:
                return cls._decode_object(obj)
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