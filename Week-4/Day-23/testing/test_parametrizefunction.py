import pytest
import source.mathematics as maths

# Concept : Parametrize 
# Instead of writing many tests for the same function with different inputs, we can parametrize.

@pytest.mark.maths # marks 
@pytest.mark.parametrize("a, b, result",[(1,1,2), # a=1 , b=1 => (a+b) result = 2
                                         (2,3,5),
                                         (4,5,9)])
def test_add(a,b,result):
    assert maths.add(a,b) == result
    
