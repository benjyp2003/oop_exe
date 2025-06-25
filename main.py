from shapes.Circle import Circle
from shapes.Hexagon import Hexagon
from shapes.Rectangle import Rectangle
from shapes.Square import Square
from shapes.Triangle import Triangle


def test():
    rectangle = Rectangle("10", -20)
    square = Square(10)
    triangle = Triangle(10, 20)
    circle = Circle(10)
    hexagon = Hexagon(10)

    lst = [rectangle, square, triangle, circle, hexagon]

    for shape in lst:
        print(f"{shape} \n")




test()