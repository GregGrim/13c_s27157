from square_generator import SquareGenerator

gen = SquareGenerator()
try:
    print(gen.get_squares(1, 11))
except SquareGenerator.MyException:
    print("start number is bigger than end number")
