from typing import List
from statistics import median


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    lst_less = []
    lst_equal = []
    lst_greater = []

    if len(container) > 1:
        base_elem = median(container)
        for elem in container:
            if elem < base_elem:
                lst_less.append(elem)
            elif elem == base_elem:
                lst_equal.append(elem)
            elif elem > base_elem:
                lst_greater.append(elem)
        return sort(lst_less) + lst_equal + sort(lst_greater)
    else:
        return container
