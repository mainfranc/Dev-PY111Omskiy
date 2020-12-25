from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if arr:
        len_arr = len(arr)
        len_of_curr_diap = len(arr) // 2
        beg_diap = 0
        while elem != arr[beg_diap + len_of_curr_diap - 1] and len_of_curr_diap != 1:
            if elem > arr[beg_diap + len_of_curr_diap - 1]: beg_diap += len_of_curr_diap
            if not len_of_curr_diap % 2:
                len_of_curr_diap //= 2
            else:
                len_of_curr_diap = len_of_curr_diap // 2 + 1
        if arr[beg_diap] == elem:
            return beg_diap
        if arr[beg_diap + len_of_curr_diap - 1] == elem:
            return beg_diap + len_of_curr_diap - 1
    return None
