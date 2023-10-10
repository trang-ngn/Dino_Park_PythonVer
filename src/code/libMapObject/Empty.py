from MapObjectType import MapObjectType
from MapObject import MapObject


class Empty(MapObject):
    def getType(self):
        return MapObjectType.EMPTY

    def print(self):
        return "[     ]"
