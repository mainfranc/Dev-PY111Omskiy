from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) > 1:
        mid = len(container) // 2
        left_part = container[0:mid]
        right_part = container[mid:len(container)]
        sort(left_part)
        sort(right_part)

        left_counter, right_counter, original_counter = 0, 0, 0
        while left_counter < len(left_part) and right_counter < len(right_part):
            if left_part[left_counter] < right_part[right_counter]:
                container[original_counter] = left_part[left_counter]
                left_counter += 1
            else:
                container[original_counter] = right_part[right_counter]
                right_counter += 1
            original_counter += 1

        while left_counter < len(left_part):
            container[original_counter] = left_part[left_counter]
            left_counter += 1
            original_counter += 1

        while right_counter < len(right_part):
            container[original_counter] = right_part[right_counter]
            right_counter += 1
            original_counter += 1

    return container
