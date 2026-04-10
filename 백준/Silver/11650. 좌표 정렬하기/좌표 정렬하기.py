import sys

input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

points = sorted(points, key=lambda x: (x[0], x[1]))

for point in points:
    print(*point)
