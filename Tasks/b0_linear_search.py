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
    if arr:
        min_value = arr[0]
        min_index = 0

        for i in range(1, len(arr)):
            if arr[i] < min_value:
                min_value = arr[i]
                min_index = i

        return min_index

    print(arr)
    return -1
