import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]

counter = Counter(cards)
max_count = max(counter.values())

num_list = [k for k, v in counter.items() if v == max_count]

print(min(num_list))
