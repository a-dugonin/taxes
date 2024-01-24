import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, basis, height):
        self.basis = basis
        self.height = height

    def area(self):
        return 0.5 * self.basis * self.height


circle = Circle(5)
print(circle.area)
