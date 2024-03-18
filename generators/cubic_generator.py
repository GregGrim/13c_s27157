from generators.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def gen_cubes(self, start: int, end: int) -> list[float]:
        if start > end:
            raise self.MyException()
        return [i**3 for i in range(start, end)]

    def gen_squares(self, start: int, end: int) -> list[float]:
        if start > end:
            raise self.MyException()
        return [i**2 for i in range(start, end)]
