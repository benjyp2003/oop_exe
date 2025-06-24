from shapes.shape import Shape


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__(width, height)

        self.width = width
        self.height = height


    def get_area(self):
        return self.width * self.height