def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    return 1 if n <= 2 else fib_recursive(n - 1) + fib_recursive(n - 2)




def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError

    left_value = 0
    right_value = 1

    for i in range(n):
        left_value, right_value = right_value, left_value + right_value

    print(n)
    return left_value
