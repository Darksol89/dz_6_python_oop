from source.figures import Triangle
import pytest


def test_create_triangle():
    triangle = Triangle(a=10, b=12)
    assert triangle.name == 'Triangle'


def test_triangle_angles():
    triangle = Triangle(a=5, b=7)
    assert triangle.angles == 3


def test_triangle_perimeter():
    triangle = Triangle(a=5, b=6)
    assert triangle.perimeter() == 18


def test_triangle_area():
    triangle = Triangle(a=5, b=6)
    assert triangle.area() == 15

def test_add_areas():
    triangle = Triangle(a=5, b=6)
    assert triangle.add_area(triangle) == 30

