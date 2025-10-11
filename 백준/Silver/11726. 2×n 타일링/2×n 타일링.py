import sys
from collections import deque

input = sys.stdin.readline


def fibo(n):
    a, b = 1, 2

    if n == 1:
        return a
    else:
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


N = int(input())
ans = fibo(N) % 10007

print(ans)
