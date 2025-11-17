import sys
from collections import Counter

input = sys.stdin.readline

word = input().strip().upper()
counts = Counter(word)
max_count = max(counts.values())

candidates = [char for char, count in counts.items() if count == max_count]

if len(candidates) == 1:
    print(candidates[0])
else:
    print("?")
