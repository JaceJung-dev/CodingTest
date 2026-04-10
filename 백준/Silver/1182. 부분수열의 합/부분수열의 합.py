import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(1, N + 1):
    for candidate in combinations(nums, i):
        if sum(candidate) == S:
            count += 1

print(count)

