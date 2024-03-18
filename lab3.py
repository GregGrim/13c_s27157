class SquareGenerator:
    def get_squares(self, start: int, end: int) -> list[int]:
        return [i ** 2 for i in range(start, end)]


gen = SquareGenerator()
print(gen.get_squares(1, 11))
