from Dino import Dino
from MapObject import MapObject
from MapObjectType import MapObjectType
import random


class Carnivore(Dino, MapObject):
    canMove=True
    listName = [
        "Allosaurus",
        "Dimetrodon",
        "Plesiosaurus",
        "Pterodactyl",
        "Spinosaurus",
    ]

    nextId = 0

    def __init__(self):
        self.id = Carnivore.nextId
        self.name = Carnivore.listName[Carnivore.nextId]
        Carnivore.nextId = Carnivore.nextId + 1

    def getType(self):
        return MapObjectType.CARNIVORE

    def print(self):
        return "\033[91m[C:" + Dino.__str__(self) + "]\033[0m"

    def attemptEat(self):
        return random.random() < 1 / 3
    
    def canBeEaten(self):
        return False
    def canMove(self):
        return True
    
    
