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

