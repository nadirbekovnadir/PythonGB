from abc import ABC, abstractmethod, abstractproperty


class Clothes(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def consumption(self):
        pass

    # Мало смысла добавлять проперти сюда
    # Только в качестве соглашения
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size

    def consumption(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.__height = height

    def consumption(self):
        return 2 * self.__height + 0.3


c1 = Coat("Coat1", 2)
print(f"Coat: {c1.name} - {c1.consumption():0.3f}")

c2 = Costume("Costume1", 3)
print(f"Coat: {c2.name} - {c2.consumption():0.3f}")
