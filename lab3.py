from square_generator.cubic_generator import CubicGenerator
from square_generator.square_generator import SquareGenerator

sq_gen = SquareGenerator()
cub_gen = CubicGenerator()
try:
    print(sq_gen.get_squares(1, 11))
    print(cub_gen.get_cubes(1, 11))

except SquareGenerator.MyException:
    print("start number is bigger than end number")




