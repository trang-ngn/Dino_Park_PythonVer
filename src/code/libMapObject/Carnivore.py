import sys
sys.path.append('/Users/trangnguyen/ProjectsCollection/Dino_Park_PythonVer/src/code/libMapObject')

from Dino import Dino
from MapObject import MapObject
from MapObjectType import MapObjectType
import random


class Carnivore(Dino, MapObject) :
    _listName = [
        "Allosaurus",
        "Dimetrodon",
        "Plesiosaurus",
        "Pterodactyl",
        "Spinosaurus",
    ]

    __nextId = 0


    def __init__(self)-> None:
        super().__init__()
        self.id = Carnivore.__nextId
        self.name = Carnivore._listName[Carnivore.__nextId]
        Carnivore.nextId = Carnivore.__nextId + 1

    def getType(self)-> MapObjectType:
        return MapObjectType.CARNIVORE

    def print(self)-> str:
        return "\033[91m[C:" + str(self) + "]\033[0m"

    @staticmethod
    def attemptEat()-> bool:
        return random.random() < 1 / 3
    
  
    
    
