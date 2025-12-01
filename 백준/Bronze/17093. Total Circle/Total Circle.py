import sys

input = sys.stdin.readline


N, M = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(M)]

max_radius_square = -1
for x1, y1 in Q:
    for x2, y2 in P:
        radius_square = (x2 - x1) ** 2 + (y2 - y1) ** 2
        max_radius_square = max(max_radius_square, radius_square)

print(max_radius_square)
