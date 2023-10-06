from abc import ABC, abstractmethod


class Dino(ABC):
    
    hasMoved = False
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def __str__(self):
        return self.name[0] + ("0" if self.id < 10 else "") + str(self.id)
