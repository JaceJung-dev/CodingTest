import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    V = list(map(int, input().split()))

    max_v = max(V[:-1])
    my_v = V[-1]

    if my_v > max_v:
        print(0)
        continue

    tmp = max_v * (my_v + X) - X * my_v
    z = tmp // max_v + 1

    if z > Y:
        print(-1)
    else:
        print(z)
