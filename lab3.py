from math import sqrt


class SquareGenerator:
    def get_squares(self, start: int, end: int) -> list[float]:
        return [sqrt(i) for i in range(start, end)]


gen = SquareGenerator()
print(gen.get_squares(1, 11))
