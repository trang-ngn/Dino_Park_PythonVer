import sys
sys.path.append('/Users/trangnguyen/ProjectsCollection/Dino_Park_PythonVer/src/code')

import random
from libMapObject.Carnivore import *
from libMapObject.Empty import *
from libMapObject.Fence import *
from libMapObject.Herbivore import *


class Map:
    def __init__(self, height: int, width:int, amountHerbi: int, amountCarni:int )->None:
        self.__height = height
        self.__width = width
        self.__amountHerbi = amountHerbi
        self.__amountCarni = amountCarni
        self.__amountFence = int(height*width * 0.1)
        
        emptyField = Empty()
        self.map = [[emptyField for j in range(width)] for i in range(height)]
        self.create_map()

    def getObjectType(self, x: int, y: int) -> MapObjectType:
        return (
            self.map[x][y].getType() if x in range(self.__height) and y in range(self.__width) else None
        )
    def getObject(self, x: int, y: int)-> MapObject:
        return (
           self.map[x][y]if x in range(self.__height) and y in range(self.__width) else None
        )

    def __generate_objects_on_map(self, object: MapObject):
        while True:
            x, y = random.randint(0, self.__height - 1), random.randint(0, self.__width - 1)
            if self.map[x][y].getType() == MapObjectType.EMPTY:
                self.map[x][y] = object
                break

    def __place_objects_random_on_map(self, object: MapObject, amount: int):
        for i in range(amount):
            self.__generate_objects_on_map(object())

    def contains_dino(self, dino: MapObjectType):
        for row in self.map:
            for cell in row:
                if cell.getType()==dino:
                    return True
        return False

   
    def create_map(self):
        self.__place_objects_random_on_map(Carnivore, self.__amountCarni)
        self.__place_objects_random_on_map(Herbivore, self.__amountHerbi)
        self.__place_objects_random_on_map(Fence, self.__amountFence)


    def __str__(self):
        output = "\n"+"-------" * self.__width + "\n"
        for i in range(self.__height):
            for j in range(self.__width):
                output = output + self.map[i][j].print()
            output = output + "\n"
        output = output + "-------" * self.__width + "\n"
        return output


if __name__ =="__main__":
    map = Map(10, 10, 10, 10)
    map.createMap()
    print(map)
    

