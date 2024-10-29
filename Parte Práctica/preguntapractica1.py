from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius=1.0):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side=1.0):
        self.side = side

    def area(self):
        return self.side * self.side


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)


# Ejemplo de uso
shapes = [Circle(), Square()]
calculator = AreaCalculator(shapes)
print(f"Área total: {calculator.total_area()}")
