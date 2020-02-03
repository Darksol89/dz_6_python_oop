"""Tests for Circle"""
from source.figures import Circle, Triangle

import pytest


def test_create_circle():
    """Create new Circle figure"""
    circle = Circle(radius=10)
    assert circle.name == 'Circle'


def test_circle_angles():
    """Create Circle without angles"""
    circle = Circle(radius=10)
    assert circle.angles == 0


def test_circle_perimeter():
    """Checking Circle perimeter calculation"""
    circle = Circle(radius=10)
    assert circle.perimeter() == 62


def test_circle_area():
    """Checking Circle area calculation"""
    circle = Circle(radius=10)
    assert circle.area() == 314


def test_add_areas():
    """Checking sum function for two figure areas"""
    circle = Circle(radius=10)
    triangle = Triangle(a=5, b=6)
    assert circle.add_area(triangle) == 329


def test_add_areas_error():
    """Checking AttributeError raises with try of sum invalid variable"""
    var = 10
    circle = Circle(radius=10)
    with pytest.raises(AttributeError):
        circle.add_area(var)
