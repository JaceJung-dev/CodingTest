import sys

input = sys.stdin.readline

N, C = map(int, input().split())
fruits = list(map(int, input().split()))

max_count = 0

for i in range(N):
    total = 0
    count = 0

    for j in range(i, N):
        if total + fruits[j] <= C:
            total += fruits[j]
            count += 1

    max_count = max(max_count, count)

print(max_count)
