import sys
from math import factorial

input = sys.stdin.readline

N, A, B, C = map(int, input().split())
total_car = A + B + C

cases = 0
if total_car <= N:
    cases = factorial(N) // (
        factorial(N - total_car) * factorial(A) * factorial(B) * factorial(C)
    )

print(cases)
