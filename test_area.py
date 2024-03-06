import pytest
from area import rectangle_area, circle_area, triangle_area


# Test cases for the area functions for the rectangle, circle, and triangle
def test_rectangle_area():
    assert rectangle_area(5, 3) == 15
    assert rectangle_area(3, 5) == 15
    assert rectangle_area(0, 0) == 0
    assert rectangle_area(0, 5) == 0
    assert rectangle_area(5, 0) == 0

def test_circle_area():
    assert round(circle_area(3), 2) == 28.27
    assert round(circle_area(5), 2) == 78.54
    assert round(circle_area(0), 2) == 0

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(3, 5) == 7.5
    assert triangle_area(0, 0) == 0
    assert triangle_area(0, 5) == 0
    assert triangle_area(5, 0) == 0


# Test cases for the area functions for the rectangle, circle, and triangle with negative values
def test_rectangle_area_negative():
    with pytest.raises(ValueError):
        rectangle_area(-5, 3)
    with pytest.raises(ValueError):
        rectangle_area(5, -3)
    with pytest.raises(ValueError):
        rectangle_area(-5, -3)

def test_circle_area_negative():
    with pytest.raises(ValueError):
        circle_area(-3)

def test_triangle_area_negative():
    with pytest.raises(ValueError):
        triangle_area(-5, 3)
    with pytest.raises(ValueError):
        triangle_area(5, -3)
    with pytest.raises(ValueError):
        triangle_area(-5, -3)

