from generators.cubic_generator import CubicGenerator
from generators.square_generator import SquareGenerator


cub_gen = CubicGenerator()
try:
    print(cub_gen.gen_cubes(1, 11))

except SquareGenerator.MyException:
    print("start number is bigger than end number")




