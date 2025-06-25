from shapes.Square import Square
import math

class Hexagon(Square):

    def get_area(self):
        return (3 * math.sqrt(3)) / 2 * self.width ** 2

    def get_perimeter(self):
        return self.width * 6

