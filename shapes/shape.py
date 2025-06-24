from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        pass

