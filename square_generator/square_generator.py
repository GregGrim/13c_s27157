from abc import ABC, abstractmethod
from math import sqrt


class SquareGenerator(ABC):
    class MyException(Exception):
        pass

    @abstractmethod
    def get_squares(self, start: int, end: int):
        pass
