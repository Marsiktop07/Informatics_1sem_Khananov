from functools import lru_cache


cache = [1, 1]
# @lru_cache()
def fib(n, cache):
    if n == 0 or n == 1:
        cache[n] = 1
        return 1
    if cache[n] != 0:
        return cache[n]
    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return cache[n]
n = int(input('Считать до: '))
cache = [0 for i in range(n + 1)]
print(fib(n, cache))