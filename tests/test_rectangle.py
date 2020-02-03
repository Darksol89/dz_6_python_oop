"""Tests for Rectangle"""
from source.figures import Rectangle
import pytest


@pytest.mark.parametrize('a, b', [(10, 5), (5, 10), (10, 10)])
def test_create_rectangle_with_valid_values(a, b):
    """Create new Rectangle figure"""
    if a > b:
        rectangle = Rectangle(a, b)
        assert rectangle.name == 'Rectangle'
    elif a < b:
        rectangle = Rectangle(a, b)
        assert rectangle.name == 'Rectangle'
    elif a == b:
        pytest.raises(ValueError)


def test_rectangle_angles():
    """Create Rectangle with 4 angles"""
    rectangle = Rectangle(a=10, b=5)
    assert rectangle.angles == 4


def test_rectangle_perimeter():
    """Checking Rectangle perimeter calculation"""
    rectangle = Rectangle(a=10, b=5)
    assert rectangle.perimeter() == 30


def test_rectangle_area():
    """Checking Rectangle area calculation"""
    rectangle = Rectangle(a=10, b=5)
    assert rectangle.area() == 50


def test_add_areas():
    """Checking sum function for two figure areas"""
    rectangle = Rectangle(a=10, b=5)
    assert rectangle.add_area(rectangle) == 100


def test_add_areas_error():
    """Checking AttributeError raises with try of sum invalid variable"""
    var = 10
    rectangle = Rectangle(a=10, b=5)
    with pytest.raises(AttributeError):
        rectangle.add_area(var)
