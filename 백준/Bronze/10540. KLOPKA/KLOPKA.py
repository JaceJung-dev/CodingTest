import sys
input = sys.stdin.readline

N = int(input())

min_x, max_x = float("inf"), float("-inf")
min_y, max_y = float("inf"), float("-inf")

for _ in range(N):
    x, y = map(int, input().split())
    min_x = min(x, min_x)
    max_x = max(x, max_x)
    min_y = min(y, min_y)
    max_y = max(y, max_y)

print(max(max_x - min_x, max_y - min_y) ** 2)