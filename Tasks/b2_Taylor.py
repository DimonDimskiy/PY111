"""
Taylor series
"""
from typing import Union
import math

ACCURACY = 10


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """

    value = 0
    for n in range(ACCURACY):
        value += math.pow(x, n)/math.factorial(n)

    print(x)
    return value


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    value = 0
    for n in range(ACCURACY):
        value += math.pow(-1, n) * math.pow(x, 2*n+1) / math.factorial(2*n+1)
    print(x)
    return value
