import sys
import time
from contextlib import contextmanager

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


@contextmanager
def elapsed_time():
    start_time = time.perf_counter()
    yield
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"Elapsed_time: {elapsed_time:.6f}")


def fibo1(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


def fibo2(n):
    arr = [-1] * (n + 2)  # n+2는 n=0일 때 arr[1]에 접근할 수 있게 하기 위해

    arr[0], arr[1] = 0, 1

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


def fibo3(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibo3(n - 1) + fibo3(n - 2)


def fibo4(n):
    global arr

    if arr[n] != -1:
        return arr[n]

    arr[n] = fibo4(n - 1) + fibo4(n - 2)
    return arr[n]


N = int(input())

arr = [-1] * (N + 2)
arr[0], arr[1] = 0, 1

with elapsed_time():
    print(fibo1(N))

with elapsed_time():
    print(fibo2(N))

with elapsed_time():
    print(fibo3(N))

with elapsed_time():
    print(fibo4(N))
