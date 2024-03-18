from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    class MyException(Exception):
        pass

    @abstractmethod
    def gen_squares(self, start: int, end: int):
        pass
