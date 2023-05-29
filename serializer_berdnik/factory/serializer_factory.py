from typing import Literal

from ..serializers import JsonSerializer, XmlSerializer


class SerializerFactory:
    _serializers_map = {
        "json": JsonSerializer,
        "xml": XmlSerializer,
    }

    @classmethod
    def create_serializer(cls, serializer_type: Literal["json", "xml"]):
        serializer = cls._serializers_map.get(serializer_type)

        if serializer is None:
            raise Exception(f"No such serializer format: {serializer_type}")

        return serializer
