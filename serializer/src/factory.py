from scr.constants import JSON_DATA_TYPE, XML_DATA_TYPE
from scr.json_serializer import JsonSerializer
from scr.xml_serializer import XmlSerializer

class SerializerFactory:
    @staticmethod #
    def create_serializer(serializer_type):
        if serializer_type == JSON_DATA_TYPE:
            return JsonSerializer()
        
        elif serializer_type == XML_DATA_TYPE:
            return XmlSerializer()