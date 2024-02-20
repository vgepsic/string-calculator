from calculate.operators import Operators
import pytest

# Addition Tests

def test_simple_addition():
    # arrange
    sut = Operators()
    operation = "7.5+8"
    expected_value = 15.5
    # act
    returned_value = sut.addition(operation)
    # assert
    assert returned_value == expected_value

@pytest.mark.parametrize("operation, expected_value", [
    ("7+8", 15),        # test case 1
    ("1+2+3", 6),       # test case 2
    ("1+2+3+4", 10),    # test case 3
    ("1+2+5", 8),       # test case 4
    ("1+2+0", 3),       # test case 5
])
def test_multiple_addition(operation, expected_value):
    # arrange
    sut = Operators()
    # act
    returned_value = sut.addition(operation)
    # assert
    assert returned_value == expected_value
