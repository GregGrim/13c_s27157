from math import sqrt


class SquareGenerator:
    class MyException(Exception):
        pass

    def get_squares(self, start: int, end: int) -> list[float]:
        if start > end:
            raise self.MyException()
        return [sqrt(i) for i in range(start, end)]


gen = SquareGenerator()
try:
    print(gen.get_squares(1, 11))
except SquareGenerator.MyException:
    print("start number is bigger than end number")
