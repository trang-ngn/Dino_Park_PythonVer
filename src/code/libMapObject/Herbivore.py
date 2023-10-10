from Dino import Dino
from MapObject import MapObject
from MapObjectType import MapObjectType


class Herbivore(Dino, MapObject):
    _listName = [
        "Achelousaurus",
        "Begyptosaurus",
        "Agilisaurus",
        "Alamosaurus",
        "Anchisaurus",
        "Albertaceratops",
        "Amargasaurus",
        "Ammosaurus",
        "Ampelosaurus",
        "Amygdalodon",
        "Anchiceratops",
        "Ankylosaurus",
        "Antarctosaurus",
        "Apatosaurus",
        "Aragosaurus",
        "Aralosaurus",
        "Archaeoceratops",
        "Argentinosaurus",
        "Arrhinoceratops",
        "Atlascocosaurus",
    ]
    __nextId = 0

    def __init__(self) -> None:
        super().__init__()
        self.id = Herbivore.__nextId
        self.name = Herbivore._listName[self.id]
        Herbivore.nextId = Herbivore.__nextId + 1

    def getType(self) -> MapObjectType:
        return MapObjectType.HERBIVORE

    def print(self) -> str:
        return "\033[33m[H:" + str(self) + "]\033[0m"
