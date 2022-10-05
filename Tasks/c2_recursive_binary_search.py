from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, l_b: int = 0, r_b: int = None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if r_b is None:
        r_b = len(arr) - 1

    if elem == arr[l_b]:
        return l_b
    if elem == arr[r_b]:
        while arr[r_b] == arr[r_b - 1]:
            r_b -= 1
        return r_b

    mid = (l_b + r_b) // 2

    if mid == l_b or mid == r_b:
        return None

    if elem == arr[mid]:
        while arr[mid] == arr[mid - 1]:
            mid -= 1
        return mid

    return binary_search(elem, arr, l_b, mid) if elem < arr[mid] else binary_search(elem, arr, mid, r_b)

    print(elem, arr)
    return None
