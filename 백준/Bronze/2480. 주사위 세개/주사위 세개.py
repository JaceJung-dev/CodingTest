import sys
from collections import Counter

input = sys.stdin.readline

nums = list(map(int, input().split()))
counts = Counter(nums)

if len(counts) == 1:
    num = nums[0]
    prize = 10000 + num * 1000
elif len(counts) == 2:
    for k, v in counts.items():
        if v == 2:
            num = k
            break
    prize = 1000 + 100 * num
elif len(counts) == 3:
    num = max(nums)
    prize = num * 100

print(prize)
