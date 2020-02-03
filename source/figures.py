"""Creating are different geometry figures and getting their perimeter and area."""
import math


class GeometryFigure:
    """Class for geometry figure"""
    name = None
    angles = None
    perimeter = None
    area = None

    def __init__(self, name, angles):
        """Class constructor for geometry figure"""
        self.name = name
        self.angles = angles

    def get_name_and_angles(self):
        if self.angles > 0:
            return f'{self.name} with {self.angles} angles'
        else:
            return f'{self.name}'

    def add_area(self, other_figure):
        """The sum of the areas different figures"""
        if isinstance(other_figure, GeometryFigure):
            sum_figures = self.area() + other_figure.area()
            return sum_figures
        else:
            raise AttributeError('Function got unknown class')


class Triangle(GeometryFigure):
    """Class for Triangle"""

    def __init__(self, a, b):
        """Constructor for Triangle creating"""
        super().__init__(name='Triangle', angles=3)
        self.a = a
        self.b = b

    def perimeter(self):
        """Perimeter calculation"""
        c = math.sqrt(self.a ** 2 + self.b ** 2)
        perimeter = self.a + self.b + c
        print(f'Perimeter {self.get_name_and_angles()} is {int(perimeter)}')
        return int(perimeter)

    def area(self):
        """Area calculation"""
        area = 1 / 2 * self.a * self.b
        print(f'Area {self.get_name_and_angles()} is {int(area)}')
        return int(area)


class Square(GeometryFigure):
    """Class for Square"""

    def __init__(self, a):
        """Constructor for Square creating"""
        super().__init__(name='Square', angles=4)
        self.a = a

    def perimeter(self):
        """Perimeter calculation"""
        perimeter = 4 * self.a
        print(f'Perimeter {self.get_name_and_angles()} is {int(perimeter)}')
        return int(perimeter)

    def area(self):
        """Area calculation"""
        area = self.a ** 2
        print(f'Area {self.get_name_and_angles()} is {int(area)}')
        return int(area)


class Rectangle(GeometryFigure):
    """Class for Rectangle"""

    def __init__(self, a, b):
        """Constructor for Rectangle creating"""
        super().__init__(name='Rectangle', angles=4)
        self.a = a
        self.b = b
        if a == b:
            raise ValueError('One side figure should be more than other side')

    def perimeter(self):
        """Perimeter calculation"""
        perimeter = 2 * self.a + 2 * self.b
        print(f'Perimeter {self.get_name_and_angles()} is {int(perimeter)}')
        return int(perimeter)

    def area(self):
        """Area calculation"""
        area = self.a * self.b
        print(f'Area {self.get_name_and_angles()} is {int(area)}')
        return int(area)


class Circle(GeometryFigure):
    """Class for Circle"""

    def __init__(self, radius):
        """Constructor for Circle creating"""
        super().__init__(name='Circle', angles=0)
        self.radius = radius

    def perimeter(self):
        """Perimeter calculation"""
        perimeter = self.radius * 2 * math.pi
        print(f'Perimeter {self.get_name_and_angles()} is {int(perimeter)}')
        return int(perimeter)

    def area(self):
        """Area calculation"""
        area = self.radius ** 2 * math.pi
        print(f'Area {self.get_name_and_angles()} is {int(area)}')
        return int(area)


if __name__ == "__main__":
    triangle = Triangle(a=5, b=6)
    square = Square(a=4)
    rectangle = Rectangle(a=6, b=3)
    circle = Circle(radius=1.5)
