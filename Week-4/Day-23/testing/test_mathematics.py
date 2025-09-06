import pytest
import source.mathematics as maths

# classic function based testing

def test_add():
    result = maths.add(1, 2)
    assert result == 3
    
def test_divide():
    result = maths.divide(4,2)
    assert result == 4

def test_divide_withzero():
    with pytest.raises(ZeroDivisionError):
        result = maths.divide(4,0)
