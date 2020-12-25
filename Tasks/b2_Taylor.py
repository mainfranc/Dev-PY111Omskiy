"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    result = 0
    for i in range(10):
        result += x ** i / fact_(i)
    return result


def fact_(n):
    if n in fact_.cache.keys():
        return fact_.cache[n]
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


fact_.cache = {}


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    result = x
    for i in range(3, 15, 2):
        result += (-1) ** ((i - 1) / 2) * (x ** i) / fact_(i)
    return result
