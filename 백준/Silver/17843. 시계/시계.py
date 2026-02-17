import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    h, m, s = map(int, input().split())

    oa = 30 * h + (m / 2) + (s / 120)
    ob = 6 * m + (s / 10)
    oc = 6 * s

    A = abs(oa - ob)
    B = abs(ob - oc)
    C = abs(oc - oa)

    A = min(A, 360 - A)
    B = min(B, 360 - B)
    C = min(C, 360 - C)

    print(f"{min(A, B, C):.6f}")
