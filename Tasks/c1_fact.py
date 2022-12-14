def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError

    return 1 if n <= 1 else factorial_recursive(n-1) * n


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """

    if n < 0:
        raise ValueError

    current_value = 1
    for i in range(1, n + 1):
        current_value *= i

    return current_value
