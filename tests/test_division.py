from main import division
import pytest


@pytest.mark.parametrize("num1, num2, result", [(10, 5, 2), (50, 10, 5), (18, 6, 3)])
def test_division(num1, num2, result):
    assert division(num1, num2) == result
