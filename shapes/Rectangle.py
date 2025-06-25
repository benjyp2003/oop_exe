from shapes.shape import Shape


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__(width, height)
        try:
            self.width = abs(int(width))
            self.height = abs(int(height))

        except ValueError as ex:
            raise ValueError ('Width and Height can be numbers only ')


    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width + self.height
