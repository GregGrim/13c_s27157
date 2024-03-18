from square_generator.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def get_cubes(self, start: int, end: int) -> list[float]:
        if start > end:
            raise self.MyException()
        return [i**3 for i in range(start, end)]

    def get_squares(self, start: int, end: int) -> list[float]:
        if start > end:
            raise self.MyException()
        return [i**2 for i in range(start, end)]