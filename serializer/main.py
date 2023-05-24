from src.factory import Factory
from src.constants import JSON_DATA_TYPE, XML_DATA_TYPE
import src.complement as cmpl

serializer = Factory.create_serializer(JSON_DATA_TYPE)
