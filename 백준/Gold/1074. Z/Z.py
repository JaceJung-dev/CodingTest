import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def calculate(N, r, c):
    if N == 0:
        return 0

    half = 2 ** (N - 1)

    # 2사분면
    if r < half and c < half:
        quadrant = 0
    # 1사분면
    elif r < half and c >= half:
        quadrant = 1
        c -= half
    # 3사분면
    elif r >= half and c < half:
        quadrant = 2
        r -= half
    # 4사분면
    else:
        quadrant = 3
        r -= half
        c -= half

    return quadrant * (half * half) + calculate(N - 1, r, c)


N, r, c = map(int, input().split())
print(calculate(N, r, c))
