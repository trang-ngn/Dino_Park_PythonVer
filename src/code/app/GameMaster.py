import sys

sys.path.append("/Users/trangnguyen/ProjectsCollection/Dino_Park_PythonVer/src/code")


from libMap.Map import *

import random
import time


class CheckNeighbor:
    def __init__(self, dino_map: Map) -> None:
        self.__dino_map = dino_map

    def has_desired_object(self, type: MapObjectType, x: int, y: int) -> bool:
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for element in directions:
            new_x, new_y = element[0] + x, element[1] + y
            if self.__dino_map.getObjectType(new_x, new_y) == type:
                return True
        return False

    def get_desired_object(self, type: MapObjectType, x: int, y: int) -> list[int]:
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        while True:
            element = random.choice(directions)
            new_x, new_y = element[0] + x, element[1] + y
            if self.__dino_map.getObjectType(new_x, new_y) == type:
                break
        return [new_x, new_y]


class DinoEat:
    def __init__(self, dino_map: Map, check_neighbor: CheckNeighbor) -> None:
        self.__dino_map = dino_map
        self.__check_neighbor = check_neighbor

    def __each_carni_eats_herbi(self, x: int, y: int) -> None:
        if self.__check_neighbor.has_desired_object(MapObjectType.HERBIVORE, x, y):
            position = self.__check_neighbor.get_desired_object(
                MapObjectType.HERBIVORE, x, y
            )
            if Carnivore.attemptEat():
                self.__dino_map.map[position[0]][position[1]] = Empty()

    def dinos_eat_in_day(self) -> None:
        for x, row in enumerate(self.__dino_map.map):
            for y, obj in enumerate(row):
                if obj.getType() == MapObjectType.CARNIVORE:
                    self.__each_carni_eats_herbi(x, y)


class DinoMove:
    def __init__(self, dino_map: Map, check_neighbor: CheckNeighbor) -> None:
        self.__dino_map = dino_map
        self.__check_neighbor = check_neighbor

    def __each_dino_moves(self, dino: Dino, x: int, y: int):
        if not dino.has_moved and self.__check_neighbor.has_desired_object(
            MapObjectType.EMPTY, x, y
        ):
            dino.has_moved = True
            [new_x, new_y] = self.__check_neighbor.get_desired_object(
                MapObjectType.EMPTY, x, y
            )
            self.__dino_map.map[new_x][new_y] = self.__dino_map.map[x][y]
            self.__dino_map.map[x][y] = Empty()

    def __reset_moving_state(self)-> None:
        for row in self.__dino_map.map:
            for obj in row:
                if isinstance(obj, Dino):
                    obj.has_moved = False

    def dino_moves_in_day(self)-> None:
        for x, row in enumerate(self.__dino_map.map):
            for y, obj in enumerate(row):
                if isinstance(obj, Dino):
                    self.__each_dino_moves(obj, x, y)

        self.__reset_moving_state()


class DinoStatistic:
    def __init__(self, dino_map: Map) -> None:
        self.__dino_map = dino_map

    def __print_dino_list(self, dino: MapObjectType)->None:
        print(f"{dino.name.capitalize()} still alive: ")
        for row in self.__dino_map.map:
            for obj in row:
                if obj.getType() == dino:
                    print(obj.print(), end=" ")

    def __print_dino_amount(self, type: MapObjectType)->None:
        dinoNum = sum(
            sum(1 for cell in row if cell.getType() == type)
            for row in self.__dino_map.map
        )
        print(f"\nAmount of {type.name.capitalize()} = {dinoNum}")

    def print_dino_statistic(self)-> None:
        self.__print_dino_list(MapObjectType.CARNIVORE)
        self.__print_dino_amount(MapObjectType.CARNIVORE)
        self.__print_dino_list(MapObjectType.HERBIVORE)
        self.__print_dino_amount(MapObjectType.HERBIVORE)

    def print_end_state(self, days: int)->None:
        print(self.__dino_map)
        self.__print_dino_amount(MapObjectType.CARNIVORE)
        self.__print_dino_amount(MapObjectType.HERBIVORE)
        print("Total rounds= ", days)


class GameMaster:
    def __init__(self, dino_map: Map)->None:
        self.dino_map = dino_map
        self.check_neighbor = CheckNeighbor(dino_map)
        self.dinos_eat = DinoEat(dino_map, self.check_neighbor)
        self.dinos_move = DinoMove(dino_map, self.check_neighbor)
        self.statistic_dinos = DinoStatistic(dino_map)

    def game_loop(self) -> None:
        day_num = 0
        while self.dino_map.contains_dino(MapObjectType.HERBIVORE):
            print(self.dino_map)
            self.statistic_dinos.print_dino_statistic()
            self.dinos_eat.dinos_eat_in_day()
            self.dinos_move.dino_moves_in_day()

            day_num += 1
            # time.sleep(1)
        self.statistic_dinos.print_end_state(day_num)


if __name__ == "__main__":
    dino_map = Map(5, 5, 3, 1)
    game_engine = GameMaster(dino_map)
    game_engine.game_loop()
