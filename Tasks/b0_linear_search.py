"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_elem = arr[0]
    min_elem_ind = -1
    if arr:
        for i in range(1, len(arr)):
            min_elem = min(min_elem, arr[i])
            if min_elem == arr[i]:
                min_elem_ind = i
    return min_elem_ind
