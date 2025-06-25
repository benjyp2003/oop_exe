from shapes.Circle import Circle
from shapes.Hexagon import Hexagon
from shapes.Rectangle import Rectangle
from shapes.Square import Square
from shapes.Triangle import Triangle


def test():
    rectangle = Rectangle("1", 2.0)
    square = Square(1)
    triangle = Triangle(1, 2.5, 2, 1.5)
    circle = Circle(10)
    hexagon = Hexagon(10)

    big_rec = Rectangle(rectangle + square, square * 2)
    small_rec = Rectangle(rectangle // 2, big_rec // 4)

    print(small_rec >= big_rec)
    print(circle < hexagon)
    print(triangle == triangle)
    print(bool(circle))

    wid, height = rectangle

    lst = [rectangle, square, triangle, circle, hexagon]

    for shape in lst:
        print(f"{shape} \n")




test()