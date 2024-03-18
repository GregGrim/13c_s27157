from math import sqrt


class SquareGenerator:
    class MyException(Exception):
        pass

    def get_squares(self, start: int, end: int) -> list[float]:
        if start > end:
            raise self.MyException()
        return [i**2 for i in range(start, end)]
