from shapes.Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, width):
        super().__init__(width, width)

