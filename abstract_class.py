import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Базовый абстрактный класс для создания фигур. Имеет абстрактный метод area вычисляющий площадь фигуры
    """
    @abstractmethod
    def area(self) -> None:
        """
        Абстрактный метод, позволяющий вычислять площадь фигуры. Требует переопределения в дочерних классах.
        :return: None
        """
        pass


class Circle(Shape):
    """
    Дочерний класс Circle. Родитель Shape. Позволяет создать фигуру круг
    Аргументы:
        radius (int | float) - передается радиус круга
    """
    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    @property
    def area(self) -> int | float:
        """
        Метод позволяет вычислить площадь круга
        :return: int | float
        """
        return math.pi * self.radius**2


class Rectangle(Shape):
    """
    Дочерний класс Rectangle. Родитель Shape. Позволяет создать фигуру прямоугольник
    Аргументы:
        side_a (int | float) - длина стороны a
        side_b (int | float) - длина стороны b
    """
    def __init__(self, side_a: int | float, side_b: int | float) -> None:
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self) -> int | float:
        """
        Метод позволяет вычислить площадь прямоугольника
        :return: int | float
        """
        return self.side_a * self.side_b


class Triangle(Shape):
    """
    Дочерний класс Triangle. Родитель Shape. Позволяет создать фигуру треугольник
    Аргументы:
        basis (int | float) - длина основания треугольника
        height (int | float) - длина стороны треугольника
    """
    def __init__(self, basis: int | float, height: int | float) -> None:
        self.basis = basis
        self.height = height

    @property
    def area(self) -> int | float:
        """
        Метод позволяет вычислить площадь треугольника
        :return: int | float
        """
        return 0.5 * self.basis * self.height


def main():
    circle = Circle(5)
    triangle = Triangle(3, 5)
    rectangle = Rectangle(4, 8)
    print(circle.area)
    print(triangle.area)
    print(rectangle.area)


if __name__ == '__main__':
    main()
