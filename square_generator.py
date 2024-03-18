from math import sqrt


class SquareGenerator:
    class MyException(Exception):
        pass

    def get_squares(self, start: int, end: int) -> list[float]:
        if start > end:
            raise self.MyException()
        return [sqrt(i) for i in range(start, end)]
