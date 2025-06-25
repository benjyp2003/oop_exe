from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def __init__(self, width: float, height: float):
        try:
            self.width = abs(float(width))
            self.height = abs(float(height))

        except ValueError as ex:
            raise ValueError ('Width and Height can be numbers only ')

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


    def __iadd__(self, other: 'Shape'):
        """
        Add two shapes to one big one.

        Args:
            other: (Shape)

        """
        self.width += other.width
        self.height += other.height


    def __add__(self, other: 'Shape'):
        """
        Sums the area of two shapes.

        Args:
            other: (Shape)
        returns:
            The area of one shape + other shape.
        """
        return self.get_area() * 2


    def __sub__(self, other: 'Shape'):
        """
        Subs the area of two shapes.

        Args:
            other: (Shape)
        returns:
            The area of one shape - other shape.
        """
        return abs(self.get_area() - other.get_area())


    def __mul__(self, other: int):
        """
        Multiplies the area of a shape by a given number.

        Args:
            other: (int)
        :returns:
            Mult of a shape area by a given number.
        """
        return self.get_area() * other


    def __floordiv__(self, other: int):
            """
            Divides the area of a shape by a given number.

            Args:
                other: (int)
            :returns:
                Div of a shape area by a given number (floors the result).
            """
            return self.get_area() // other


    def __truediv__(self, other: int):
            """
            Divides the area of a shape by a given number.

            Args:
                other: (int)
            :returns:
                Div of a shape area by a given number.
            """
            return self.get_area() / other


    def __ge__(self, other):
        """
        Compare the areas of two shapes.

        :param other: (Shape)
        :return: true if the first shapes area is bigger, else false.
        """
        return self.get_area() >= other.get_area()


    def __lt__(self, other):
        """
        Compare the areas of two shapes.

        :param other: (Shape)
        Return True if this shape's area is less than the other.
        """
        return self.get_area() < other.get_area()


    def __le__(self, other):
        """
        Compare the areas of two shapes.

        :param other: (Shape)
        Return True if this shape's area is less than or equal to the other.
        """
        return self.get_area() <= other.get_area()


    def __gt__(self, other):
        """
        Compare the areas of two shapes.

        :param other: (Shape)
        Return True if this shape's area is greater than the other.
        """
        return self.get_area() > other.get_area()


    def __eq__(self, other):
        """
        Compare the areas of two shapes.

        :param other: (Shape)
        Return: True if this shape's area is equal to the other.
        """
        return self.get_area() == other.get_area()


    def __ne__(self, other):
        """
        Compare the areas of two shapes.

        :param other: (Shape)
        Return True if this shape's area is not equal to the other.
        """
        return not self == other


    def __iter__(self):
        """
        Allow unpacking of width and height like: width, height = shape

        :returns A iterable obj with the width and length.
        """
        return iter((self.width, self.height))


    def __bool__(self):
        """
        Checks if the area is bigger than 0.
        :return: true if bigger, else false
        """
        return self.get_area() > 0


    def __len__(self):
        """
        :return: Length of the base side of the shape.
        """
        return self.width


    def __str__(self):
        return (f"Shape info: \n"
                f"  Name: {self.__class__.__name__} \n"
                f"  Width: {self.width} \n"
                f"  Height: {self.height if not self.__class__.__name__ == 'Hexagon' else 'Hexagon has no height.'} \n"
                f"  Area: {self.get_area()} \n"
                f"  Perimeter: {self.get_perimeter()} \n")

