
class GeometryFigure:
    """Class for geometry figure"""
    _name = None
    _angles = None
    _perimeter = None
    _area = None

    def __init__(self, name, perimeter, area, angles):
        """Class constructor for geometry figure"""
        self.name = name
        self.perimeter = perimeter
        self.area = area
        self.angles = angles
        print('Geometry figure {name} was created!')

    def __str__(self):
        return self._name
    
    def perimeter_calculation(self):
        return "{name} figure perimeter is equals {perimeter}"

    def area_calculation(self):
        return "{name} figure area is equals {area}"



class Trangle(GeometryFigure):

    def __init__(self, name, perimeter, area):
        super().__init__(name, perimeter, area, 3)
        self.name = 'Trangle'
        self.perimeter