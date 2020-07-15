import pytest


def calculate_sum(a, b):
    return a + b


@pytest.mark.parametrize("num1, num2, output",
                         [
                             (2, 2, 4),
                             (5, 5, 10),
                             (10, 20, 30)

                         ]
                         )
def test_calc_sum1(num1, num2, output):
    result = calculate_sum(num1, num2)
    assert result == output
