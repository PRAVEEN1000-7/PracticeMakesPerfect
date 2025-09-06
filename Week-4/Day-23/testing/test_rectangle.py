import pytest
import source.Shapes as shapes

# pytest fixtures
@pytest.fixture
def my_rectangle():
    rectangle = shapes.Rectangle(10,7) # setup 
    yield rectangle     # give to test
    del rectangle    # teardowm

# pytest fixtures
@pytest.fixture
def my2_rectangle():
    rectangle = shapes.Rectangle(12,8) # setup 
    yield rectangle     # give to test
    del rectangle    # teardowm

# testing rectangle area
def test_rectangleArea(my_rectangle):
    assert my_rectangle.perimeter(10,7) == 2 * (10 + 7)
    
# testing 2 rectangle objects area is not equal
def test_equals(my_rectangle, my2_rectangle):
    assert my_rectangle.area() != my2_rectangle.area()

def test_equals_three(my_rectangle, my2_rectangle, my3_rectangle):
    assert my_rectangle.area() != my2_rectangle.area() != my3_rectangle.area()