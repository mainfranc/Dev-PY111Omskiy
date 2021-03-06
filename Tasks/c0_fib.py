def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    cache = {}
    result = fib_rec_calc(n, cache)
    return result

def fib_rec_calc(n: int, cache) -> int:
    if n < 1:
        raise ValueError()
    if n == 1 or n == 2:
        return 1
    if cache.get(n):
        return cache[n]
    result =  fib_rec_calc(n-1, cache) + fib_rec_calc(n-2, cache)
    cache[n] = result
    return result




def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 1:
        raise ValueError()

    r1, r2 = 0, 1
    for i in range(0, n - 1):
        last_member = r1 + r2
        r1 = r2
        r2 = last_member
    return r2


