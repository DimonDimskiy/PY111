from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    mid_index = len(arr) // 2
    right_border = len(arr) - 1
    left_border = 0
    while left_border <= mid_index <= right_border:
        if elem > arr[mid_index]:
            left_border = mid_index + 1
            mid_index += (len(arr[mid_index:right_border]) // 2 + 1)
        if elem < arr[mid_index]:
            right_border = mid_index - 1
            mid_index -= (len(arr[left_border:mid_index]) // 2 + 1)

        if elem == arr[mid_index]:
            while arr[mid_index] == arr[mid_index - 1]:
                mid_index -= 1
            return mid_index


    print(elem, arr)
    return None
