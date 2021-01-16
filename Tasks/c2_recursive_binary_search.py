from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if not elem in arr:
        return None
    arr_beg = 0
    arr_end = len(arr) - 1
    mid = (len(arr) - 1) // 2
    if arr[mid] == elem:
        return mid
    if arr[mid + 1] == elem:
        return mid + 1
    # be present in left subarray
    elif arr[mid] > elem:
        return binary_search(elem, arr[arr_beg: mid + 1])
        # Else the element can only be present in right subarray
    else:
        return mid + 1 + binary_search(elem, arr[mid + 1: len(arr)])
