import sys

input = sys.stdin.readline

N = int(input())
stones = list(map(int, input().split()))

total = stones[0] - stones[1]
for i in range(2, N):
    if total > 0:
        total -= stones[i]
    else:
        total += stones[i]

total = abs(total)

weights = [100, 50, 20, 10, 5, 2, 1]

count = 0
for weight in weights:
    count += total // weight
    total %= weight

print(count)
