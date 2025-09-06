import pytest
import source.mathematics as maths

# Marks are like labels you put on test functions.
# They help you:
# Group tests
# Skip tests
# Run only selected tests

# Custom marks (for grouping)
@pytest.mark.maths
def test_add():
    assert maths.add(1,2) == 3
    

# Skip a test unconditionally.
@pytest.mark.skip(reason="this feature is currently broken")
def test_divide():
    assert maths.divide(1,0)