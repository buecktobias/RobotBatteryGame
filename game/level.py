import abc


class Level(abc.ABC):
    @abc.abstractmethod
    def load(self):
        pass
