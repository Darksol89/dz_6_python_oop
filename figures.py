class GeometryFigure:
    """Class for geometry figure"""
    _name = None

    def __init__(self, name):
        """Class constructor for geometry figure"""
        self.name = name
        print(f'Geometry figure {name} was created!')

    def __str__(self):
        return self._name

    def get_figure_name(self):
        return f"{self.name}"


class Triangle(GeometryFigure):

    def __init__(self, name, angles, side_1, side_2, side_3):
        super().__init__(name)
        self.angles = 3
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def triangle_perimeter_calculation(self):
        triangle_perimeter = self.side_1 + self.side_2 + self.side_3
        return f'{self.get_figure_name()} perimeter with {self.angles} angles equals {str(triangle_perimeter)}'

    @staticmethod
    def triangle_area_calculation(side_1, height):
        triangle_area = 1 / 2 * (side_1 * height)
        return f'Triangle area equals {str(triangle_area)}'


class Rectangle(GeometryFigure):

    def __init__(self, name, angles, side_1, side_2):
        super().__init__(name)
        self.angles = 4
        self.side_1 = side_1
        self.side_2 = side_2

    def rectangle_perimeter_calculation(self):
        retangle_perimeter = 2 * (self.side_1 + self.side_2)
        return f'{self.get_figure_name()} perimeter with {self.angles} angles equals {str(retangle_perimeter)}'

    def rectangle_area_calculation(self):
        rectangle_area = self.side_1 * self.side_2
        return f'{self.get_figure_name()} area with {self.angles} angles equals {str(rectangle_area)}'


class Quadrate(GeometryFigure, Rectangle):
    pass


if __name__ == '__main__':
    # triangle = Triangle(name='Triangle', angles=3, side_1=10, side_2=12, side_3=10)
    # print(Triangle.triangle_area_calculation(10, 5))
    # print(triangle.triangle_perimeter_calculation())

    rectangle = Rectangle(name='Rectangle', angles=4, side_1=10, side_2=20)
    print(rectangle.rectangle_perimeter_calculation())
    print(rectangle.rectangle_area_calculation())
