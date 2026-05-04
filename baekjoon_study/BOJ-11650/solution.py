import sys

input = sys.stdin.readline

# input
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# solve
points = sorted(points)

for x, y in points:
    print(x, y)
