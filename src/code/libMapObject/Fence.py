from MapObjectType import MapObjectType
from MapObject import MapObject


class Fence(MapObject):
    def getType(self):
        return MapObjectType.FENCE

    def print(self):
        return "\033[32m" + "[xxxxx]" + "\033[m"
