import timeit


def check_sorts():
    setup = '''
import random
from Tasks.g2_quick_sort import sort as quick_sort
from Tasks.g1_merge_sort import sort as merge_sort
from Tasks.g0_bubble_sort import sort as bubble_sort

arr = [6, -83, 39, 85, -39, -53, 52, -15, -13, -58, 18, -17, 53, -67, 72, -49, -3, -19, -68, -72, 52, 60, -41, 99, -52, -61, 7, 89, -27, 3]
sorted_arr = sorted(arr)
sorted_arr_back = sorted(arr, reverse=True)'''

    print('original sort')
    print(min(timeit.Timer('sorted(arr)', setup).repeat(10, 1000)))
    print(min(timeit.Timer('sorted(sorted_arr)', setup).repeat(10, 1000)))
    print(min(timeit.Timer('sorted(sorted_arr_back)', setup).repeat(10, 1000)))

    print('bubble sort')
    print(min(timeit.Timer('bubble_sort(arr)', setup).repeat(10, 1000)))
    print(min(timeit.Timer('bubble_sort(sorted_arr)', setup).repeat(10, 1000)))
    print(min(timeit.Timer('bubble_sort(sorted_arr_back)', setup).repeat(10, 1000)))

    print('merge sort')
    print(min(timeit.Timer('merge_sort(arr)', setup).repeat(10, 1000)))
    print(min(timeit.Timer('merge_sort(sorted_arr)', setup).repeat(10, 1000)))
    print(min(timeit.Timer('merge_sort(sorted_arr_back)', setup).repeat(10, 1000)))

    print('quick sort')
    print(min(timeit.Timer('quick_sort(arr)', setup).repeat(10, 1000)))
    print(min(timeit.Timer('quick_sort(sorted_arr)', setup).repeat(10, 1000)))
    print(min(timeit.Timer('quick_sort(sorted_arr_back)', setup).repeat(10, 1000)))


if __name__ == '__main__':
    check_sorts()