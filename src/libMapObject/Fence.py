from MapObjectType import MapObjectType
from MapObject import MapObject


class Fence(MapObject):
    canMove=False
    def getType(self):
        return MapObjectType.FENCE

    def print(self):
        return "\033[32m" + "[xxxxx]" + "\033[m"

    def canBeEaten(self):
        return False
    def canMove(self):
        return False