from square_generator.cubic_generator import CubicGenerator
from square_generator.square_generator import SquareGenerator


cub_gen = CubicGenerator()
try:
    print(cub_gen.get_cubes(1, 11))

except SquareGenerator.MyException:
    print("start number is bigger than end number")




