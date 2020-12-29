def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 1:
        raise ValueError()
    if n == 1 or n == 2:
        return 1
    if fib_recursive.cache.get(n, 0):
        return fib_recursive.cache[n]
    result =  fib_recursive(n-1) + fib_recursive(n-2)
    fib_recursive.cache[n] = result
    return result

fib_recursive.cache = {}


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 1:
        raise ValueError()

    results = [0, 1]
    for i in range(0, n - 1):
        last_res_ind = len(results) - 1
        results.append(results[last_res_ind] + results[last_res_ind - 1])
    return results[len(results) - 1]


