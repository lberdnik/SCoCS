import types

JSON_DATA_TYPE = '.json'

XML_DATA_TYPE = '.xml'

UNKNOWN_DATA_TYPE = 'Unknown type of serialization'

DEFAULT_PRIMITIVE_TYPES = (int, bool, str, float, types.NoneType)

UNSERIALIZERABLE_TYPES = (
    types.WrapperDescriptorType,    #
    types.MethodDescriptorType,     #
    types.BuiltinFunctionType,      #
    types.MappingProxyType,         #
    types.GetSetDescriptorType,     #
)

SAME_TYPE_ERROR = 'Same         type of objects!'

UNSUPPORTED_TYPE_ERROR = 'Unsupported data type: %s (%s)'
UNKNOWN_TYPE_ERROR = 'Unknown type of serialization!'

ITERATOR_TYPE = 'iterator'
BYTES_TYPE = 'bytes'
CODE_TYPE = 'code'
OBJ_TYPE = 'object'
MODULE_TYPE = 'module'
CELL_TYPE = 'cell'
FUNCTION_TYPE = 'function'
CLASS_TYPE = 'type'
SET_TYPE = 'set'
DICT_TYPE = 'dict'
TUPLE_TYPE = 'tuple'

NSERIALIZABLE_CODE_TYPES = (
    "co_positions",
    "co_lines",
    "co_exceptiontable",
    "co_lnotab",
)