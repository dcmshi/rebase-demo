def fib(n: int) -> int:
    """
    Get the nth fibonacci number
    :param n: index in the sequence to get
    :return: nth fibonacci number in the sequence
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fib_iter(n: int) -> int:
    """
    Get the nth fibonacci number iteratively
    :param n: index in the sequence to get
    :return: nth fibonacci number in the sequence
    """
    a, b, c = 0, 1, 1
    for i in range(0, n):
        a = b
        b = c
        c = a + b

    return c


def fib_decider(n: int, to_call: str = 'fib') -> int:
    """
    Gives option to call which fibonacci function to call
    :param n: position in the sequence to get
    :param to_call: which function to call
    :return: nth fibonacci number
    """
    if to_call == 'fib':
        return fib(n)
    return fib_iter(n)
