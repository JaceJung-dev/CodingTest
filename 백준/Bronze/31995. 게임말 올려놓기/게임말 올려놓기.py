import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

if N == 0 or M == 0:
    print(0)

print(2 * (N - 1) * (M - 1))
