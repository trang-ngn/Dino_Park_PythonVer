class Dino:
    def __new__(cls) -> None:
        if cls.__name__ == "Dino":
            raise TypeError("Cannot create an instance of Dino")
        return super(Dino, cls).__new__(cls)

    def __init__(self) -> None:
        self.has_moved = False

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        return self.name[0] + ("0" if self.id < 10 else "") + str(self.id)
