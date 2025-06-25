from shapes.Rectangle import Rectangle


class Triangle(Rectangle):
    def __init__(self, base, side1, side2, height: float):
        super().__init__(base, height)
        try:
            self.base = abs(float(base))
            self.side1 = abs(float(side1))
            self.side2 = abs(float(side2))

        except ValueError as ex:
            raise ValueError('Width and Height can be numbers only ')

    def get_area(self):
        return 0.5 * self.base * self.height

    def get_perimeter(self):
        return self.base + self.side1 + self.side2


    def __str__(self):
        return (f"Shape info: \n"
                f"  Name: {self.__class__.__name__} \n"
                f"  Base: {self.base} \n"
                f"  side1: {self.side1} \n"
                f"  side2: {self.side2} \n"
                f"  Height: {self.height} \n"
                f"  Area: {self.get_area()} \n"
                f"  Perimeter: {self.get_perimeter()} \n")
