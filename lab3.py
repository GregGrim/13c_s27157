
def get_squares(start: int, end: int) -> list[int]:
    return [ i**2 for i in range(start, end)]


print(get_squares(1, 11))
