from abc import ABC, abstractmethod


class MapObject(ABC):
    @abstractmethod
    def getType(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def canBeEaten(self):
        pass
    
    @abstractmethod
    def canMove(self):
        pass
    
    