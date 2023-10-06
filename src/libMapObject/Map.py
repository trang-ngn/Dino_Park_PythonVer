import random
from Carnivore import Carnivore
from Empty import Empty
from Fence import Fence
from Herbivore import Herbivore
from MapObject import MapObject
from MapObjectType import MapObjectType


class Map:
    def __init__(self, height, width, amountHerbi, amountCarni):
        self.height = height
        self.width = width
        self.amountHerbi = amountHerbi
        self.amountCarni = amountCarni
        self.amountFence = int(height*width * 0.1)

    def getObjectType(self, x: int, y: int):
        return (
            self.map[x][y].getType() if x in range(self.height) and y in range(self.width) else None
        )
    def getObject(self, x: int, y: int):
        return (
           self.map[x][y]if x in range(self.height) and y in range(self.width) else None
        )
    def setObject(self, object: MapObject, x,y):
        self.map[x][y]= object

    def fillMapWithEMptyField(self):
        emptyField = Empty()
        self.map = [[emptyField for j in range(self.width)] for i in range(self.height)]

    def generateObjectsOnMap(self, object: MapObject):
        while True:
            x, y = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if self.map[x][y].getType() == MapObjectType.EMPTY:
                self.map[x][y] = object
                break

    def placeObjectsRandomOnMap(self, object: MapObject, amount: int):
        for i in range(amount):
            self.generateObjectsOnMap(object())

    def containsDino(self, dino: MapObjectType):
        for row in self.map:
            for cell in row:
                if cell.getType()==dino:
                    return True
        return False

   
    def createMap(self):
        self.fillMapWithEMptyField()
        self.placeObjectsRandomOnMap(Carnivore, self.amountCarni)
        self.placeObjectsRandomOnMap(Herbivore, self.amountHerbi)
        self.placeObjectsRandomOnMap(Fence, self.amountFence)


    def __str__(self):
        output = "\n"+"-------" * self.width + "\n"
        for i in range(self.height):
            for j in range(self.width):
                output = output + self.map[i][j].print()
            output = output + "\n"
        output = output + "-------" * self.width + "\n"
        return output


# map = Map(10, 5, 10, 10)

# map.createMap()
# print(map)
# print(map.getObjectType(0, 0))

