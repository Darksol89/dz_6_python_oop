"""Creating are different geometry figures and getting their perimeter and area."""
import math


class GeometryFigure:
    """Class for geometry figure"""
    name = None
    angles = None
    perimeter = None
    area = None

    def __init__(self):
        """Class constructor for geometry figure"""
        self.name = None

    def add_area(self, other_figure):
        """The sum of the areas different figures"""
        if isinstance(other_figure, GeometryFigure):
            print(self.area() + other_figure.area())
        else:
            print('Unknown class')


class Triangle(GeometryFigure):
    """Class for Triangle"""

    def __init__(self, a, b):
        """Constructor for Triangle creating"""
        super().__init__()
        self.a = a
        self.b = b
        self.name = 'Triangle'
        self.angles = 3

    def perimeter(self):
        """Perimeter calculation"""
        c = math.sqrt(self.a ** 2 + self.b ** 2)
        perimeter = self.a + self.b + c
        print(f'Perimeter {self.name} with {self.angles} angles is {int(perimeter)}')
        return perimeter

    def area(self):
        """Area calculation"""
        area = 1 / 2 * self.a * self.b
        print(f'Area {self.name} with {self.angles} angles is {int(area)}')
        return area


class Square(GeometryFigure):
    """Class for Square"""

    def __init__(self, a):
        """Constructor for Square creating"""
        super().__init__()
        self.name = 'Square'
        self.angles = 4
        self.a = a

    def perimeter(self):
        """Perimeter calculation"""
        perimeter = 4 * self.a
        print(f'Perimeter {self.name} with {self.angles} angles is {int(perimeter)}')
        return perimeter

    def area(self):
        """Area calculation"""
        area = self.a ** 2
        print(f'Area {self.name} with {self.angles} angles is {int(area)}')
        return area


class Rectangle(GeometryFigure):
    """Class for Rectangle"""

    def __init__(self, a, b):
        """Constructor for Rectangle creating"""
        super().__init__()
        self.name = 'Rectangle'
        self.angles = 4
        self.a = a
        self.b = b
        if not a > b:
            raise ValueError('Value "a" cannot be less than value "b" ')

    def perimeter(self):
        """Perimeter calculation"""
        perimeter = 2 * self.a + 2 * self.b
        print(f'Perimeter {self.name} with {self.angles} angles is {int(perimeter)}')
        return perimeter

    def area(self):
        """Area calculation"""
        area = self.a * self.b
        print(f'Area {self.name} with {self.angles} angles is {int(area)}')
        return area


class Circle(GeometryFigure):
    """Class for Circle"""

    def __init__(self, radius):
        """Constructor for Circle creating"""
        super().__init__()
        self.name = 'Circle'
        self.angles = None
        self.radius = radius

    def perimeter(self):
        """Perimeter calculation"""
        perimeter = self.radius * 2 * math.pi
        print(f'Perimeter {self.name} with {self.angles} angles is {int(perimeter)}')
        return perimeter

    def area(self):
        """Area calculation"""
        area = self.radius ** 2 * math.pi
        print(f'Area {self.name} is {int(area)}')
        return area


if __name__ == "__main__":
    triangle = Triangle(a=5, b=6)
    square = Square(a=4)
    rectangle = Rectangle(a=6, b=3)
    circle = Circle(radius=1.5)

    triangle.add_area(circle)
