"""Tests for Square"""
from source.figures import Square
import pytest


def test_create_square():
    """Create new Square figure"""
    square = Square(a=10)
    assert square.name == 'Square'


def test_square_angles():
    """Create Square with 4 angles"""
    square = Square(a=10)
    assert square.angles == 4


def test_square_perimeter():
    """Checking Square perimeter calculation"""
    square = Square(a=10)
    assert square.perimeter() == 40


def test_square_area():
    """Checking Square area calculation"""
    square = Square(a=10)
    assert square.area() == 100


def test_add_areas():
    """Checking sum function for two figure areas"""
    square = Square(a=10)
    assert square.add_area(square) == 200


def test_add_areas_error():
    """Checking AttributeError raises with try of sum invalid variable"""
    var = 10
    square = Square(a=10)
    with pytest.raises(AttributeError):
        square.add_area(var)
