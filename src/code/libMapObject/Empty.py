from MapObjectType import MapObjectType
from MapObject import MapObject


class Empty(MapObject):
    def getType(self) -> MapObjectType:
        return MapObjectType.EMPTY

    def print(self) -> str:
        return "[     ]"
