import abc
from game import position


class GameObject(abc.ABC):
    def __init__(self, x, y):
        self.position = position.Position(x, y)

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def draw(self, game):
        pass
