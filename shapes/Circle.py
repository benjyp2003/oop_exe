import math
from shapes.shape import Shape

class Circle(Shape):

    def __init__(self, width):
        super().__init__(width, width)

    def get_area(self):
        return math.pi * (self.width / 2) ** 2

    def get_perimeter(self):
        return 2 * math.pi * (self.width / 2)
