from Dino import Dino
from MapObject import MapObject
from MapObjectType import MapObjectType


class Herbivore(Dino, MapObject):
    listName = [
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
    nextId = 0
    canMove=True
    
    def __init__(self):
        self.id = Herbivore.nextId
        self.name = Herbivore.listName[self.id]
        Herbivore.nextId = Herbivore.nextId + 1

    def getType(self):
        return MapObjectType.HERBIVORE

    def print(self):
        return "\033[33m[H:" + Dino.__str__(self) + "]\033[0m"

    def canBeEaten(self):
        return False
    
    def canMove(self):
        return True