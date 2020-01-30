
class GeometryFigure:
    """Class for geometry figure"""
    _name = None
    _angles = None
    _perimeter = None
    _area = None

    def __init__(self, name, angles):
        """Class constructor for geometry figure"""
        self.name = name
        self.angles = angles
        print(f'Geometry figure {name} with {angles} angles was created!')

    def __str__(self):
        return self._name
    
    def get_name_and_angles(self):
        return f"{self.name} with {self.angles} angles have "



class Trangle(GeometryFigure):

    def __init__(self, name, a, b, c):
        super().__init__(name, 3)
        self.a = a
        self.b = b
        self.c = c


    def trangle_perimeter_calculation(self):
        perimeter = self.a + self.b + self.c
        return self.get_name_and_angles() + 'perimeter = ' + str(perimeter)


if __name__ == '__main__':
    trangle = Trangle(name='Trangle', a=5, b=5, c=10)
    print(trangle.trangle_perimeter_calculation())