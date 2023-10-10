import sys

sys.path.append(
    "/Users/trangnguyen/ProjectsCollection/Dino_Park_PythonVer/src/code/libMapObject"
)
from MapObjectType import MapObjectType
from MapObject import MapObject


class Fence(MapObject):
    def getType(self) -> MapObjectType:
        return MapObjectType.FENCE

    def print(self) -> str:
        return "\033[32m" + "[xxxxx]" + "\033[m"
