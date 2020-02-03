"""Tests for Triangle"""
from source.figures import Triangle
import pytest


def test_create_triangle():
    """Create new Triangle figure"""
    triangle = Triangle(a=10, b=12)
    assert triangle.name == 'Triangle'


def test_triangle_angles():
    """Create Triangle with 3 angles"""
    triangle = Triangle(a=5, b=7)
    assert triangle.angles == 3


def test_triangle_perimeter():
    """Checking Triangle perimeter calculation"""
    triangle = Triangle(a=5, b=6)
    assert triangle.perimeter() == 18


def test_triangle_area():
    """Checking Triangle area calculation"""
    triangle = Triangle(a=5, b=6)
    assert triangle.area() == 15


def test_add_areas():
    """Checking sum function for two figure areas"""
    triangle = Triangle(a=5, b=6)
    assert triangle.add_area(triangle) == 30


def test_add_areas_error():
    """Checking AttributeError raises with try of sum invalid variable"""
    var = 10
    triangle = Triangle(a=5, b=6)
    with pytest.raises(AttributeError):
        triangle.add_area(var)
