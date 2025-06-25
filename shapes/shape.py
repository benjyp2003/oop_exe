from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def __init__(self, width: int, height: int):
        try:
            self.width = abs(int(width))
            self.height = abs(int(height))

        except ValueError as ex:
            raise ValueError ('Width and Height can be numbers only ')

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


    def __str__(self):
        return (f"Shape info: \n"
                f"  Name: {self.__class__.__name__} \n"
                f"  Width: {self.width} \n"
                f"  Height: {self.height if not self.__class__.__name__ == 'Hexagon' else 'Hexagon has no height.'} \n"
                f"  Area: {self.get_area()} \n"
                f"  Perimeter: {self.get_perimeter()}")

