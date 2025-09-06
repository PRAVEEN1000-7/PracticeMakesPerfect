import pytest
from source.Shapes import Rectangle

# conftest.py
# it is a special configuration file used to share fixtures(sometimes hooks) 
# across multiple test files without importing them manually
# works in that directory & it's sub-directory

# pytest fixtures
@pytest.fixture
def my3_rectangle():
    rectangle = Rectangle(14,9) # setup 
    yield rectangle     # give to test
    del rectangle    # teardowm
    

