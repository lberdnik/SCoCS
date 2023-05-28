import types

JSON_DATA_TYPE = '.json'

XML_DATA_TYPE = '.xml'

DEFAULT_PRIMITIVE_TYPES = (int, bool, str, float, type(None))

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
PROPERTY_TYPE = 'property'

UNSERIALIZABLE_CODE_TYPES = (
    "co_positions",
    "co_lines",
    "co_exceptiontable",
    "co_lnotab",
)

UNSERIALIZABLE_DUNDER = (
    "__mro__",
    "__base__",
    "__basicsize__",
    "__class__",
    "__dictoffset__",
    "__name__",
    "__qualname__",
    "__text_signature__",
    "__itemsize__",
    "__flags__",
    "__weakrefoffset__",
    "__objclass__",
    "__doc__"
)
