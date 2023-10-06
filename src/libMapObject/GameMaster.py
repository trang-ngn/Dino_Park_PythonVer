from Map import Map
from MapObjectType import MapObjectType
from Carnivore import Carnivore
from Empty import Empty
from Dino import Dino
import random
import time


class GameMaster:
    dinoMap = Map(10, 10, 10, 5)
    dinoMap.createMap()


class DinoControl:
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    def hasNearbyDesiredObject(self, type: MapObjectType, x, y):
        for element in self.directions:
            newX, newY = element[0] + x, element[1] + y
            if GameMaster.dinoMap.getObjectType(newX, newY) == type:
                return True
        return False

    def getNearbyDesiredObject(self, type: MapObjectType, x, y):
        while True:
            element = random.choice(self.directions)
            newX, newY = element[0] + x, element[1] + y
            if GameMaster.dinoMap.getObjectType(newX, newY) == type:
                break
        return [newX, newY]

    def eachCarniEats(self, x, y):
        if self.hasNearbyDesiredObject(MapObjectType.HERBIVORE, x, y):
            position = self.getNearbyDesiredObject(MapObjectType.HERBIVORE, x, y)
            if Carnivore.attemptEat(self):
                GameMaster.dinoMap.setObject(Empty(), position[0], position[1])

    def dinosEatInDay(self):
        for i in range(GameMaster.dinoMap.height):
            for j in range(GameMaster.dinoMap.width):
                if GameMaster.dinoMap.getObjectType(i, j) == MapObjectType.CARNIVORE:
                    self.eachCarniEats(i, j)

    def eachDinoMoves(self, dino: Dino, x, y):
        if dino.hasMoved==False and self.hasNearbyDesiredObject(MapObjectType.EMPTY, x, y):
            dino.hasMoved = True
            newPosition = self.getNearbyDesiredObject(MapObjectType.EMPTY, x, y)
            GameMaster.dinoMap.setObject(
                GameMaster.dinoMap.getObject(x, y), newPosition[0], newPosition[1]
            )
            GameMaster.dinoMap.setObject(Empty(), x, y)

    def dinoMovesInDay(self):
        for i in range(GameMaster.dinoMap.height):
            for j in range(GameMaster.dinoMap.width):
                if (
                    GameMaster.dinoMap.getObject(i, j) != None
                    and GameMaster.dinoMap.getObject(i, j).canMove()
                ):
                    self.eachDinoMoves(GameMaster.dinoMap.getObject(i, j), i, j)
      

    def resetDinosMovingState(self):
        for i in range(GameMaster.dinoMap.height):
            for j in range(GameMaster.dinoMap.width):
                if isinstance(GameMaster.dinoMap.getObject(i, j), Dino):
                    GameMaster.dinoMap.getObject(i, j).hasMoved = False


class DinoStatistic:
    def printDinoList(self, dino: MapObjectType):
        print(dino.name.capitalize(), "still alive: ")
        for i in range(GameMaster.dinoMap.height):
            for j in range(GameMaster.dinoMap.width):
                if GameMaster.dinoMap.getObjectType(i, j) == dino:
                    print(GameMaster.dinoMap.getObject(i, j).print(), end=" ")

    def printDinoAmount(self, dino: MapObjectType):
        dinoNum = 0
        for i in range(GameMaster.dinoMap.height):
            for j in range(GameMaster.dinoMap.width):
                if GameMaster.dinoMap.getObjectType(i, j) == dino:
                    dinoNum = dinoNum + 1
        print("\nAmount of", dino.name.capitalize(),"=", dinoNum)

    def printDinoStatistic(self):
        self.printDinoList(MapObjectType.CARNIVORE)
        self.printDinoAmount(MapObjectType.CARNIVORE)
        self.printDinoList(MapObjectType.HERBIVORE)
        self.printDinoAmount(MapObjectType.HERBIVORE)

    def printEndState(self, days: int):
        print(GameMaster.dinoMap)
        self.printDinoAmount(MapObjectType.CARNIVORE)
        self.printDinoAmount(MapObjectType.HERBIVORE)
        print("Total rounds= ", days)


days = 0
gameMaster = GameMaster()
dinoControl = DinoControl()
dinoStatistic = DinoStatistic()
while gameMaster.dinoMap.containsDino(MapObjectType.HERBIVORE):
    print(gameMaster.dinoMap)
    dinoControl.dinosEatInDay()
    dinoControl.dinoMovesInDay()
    dinoControl.resetDinosMovingState()
    dinoStatistic.printDinoStatistic()
    time.sleep(2)
    days = days + 1
dinoStatistic.printEndState(days)
