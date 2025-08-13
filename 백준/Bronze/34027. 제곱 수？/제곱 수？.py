import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    sqrt_N = N ** 0.5
    if sqrt_N.is_integer():
        print(1)
    else:
        print(0)