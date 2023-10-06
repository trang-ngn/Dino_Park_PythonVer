from MapObjectType import MapObjectType
from MapObject import MapObject


class Empty(MapObject):
    canMove=False
    def getType(self):
        return MapObjectType.EMPTY

    def print(self):
        return "[     ]"

    def canBeEaten(self):
        return False
    def canMove(self):
        return False
    