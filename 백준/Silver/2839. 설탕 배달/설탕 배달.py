import sys

input = sys.stdin.readline


N = int(input())
min_count = float("inf")
max_five = N // 5

for i in range(max_five, -1, -1):
    left = N - 5 * i
    if left % 3 == 0:
        count = i + left // 3
        min_count = min(min_count, count)

print(-1 if min_count == float("inf") else min_count)