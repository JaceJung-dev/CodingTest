import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    V = int(input())
    nums = [int(input()) for _ in range(V)]

    counter = Counter(nums)
    max_count = max(counter.values())

    ans_num = min(num for num, count in counter.items() if count == max_count)
    print(ans_num)

