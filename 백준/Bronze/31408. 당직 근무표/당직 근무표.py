import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
schedule = list(map(int, input().split()))

freq = Counter(schedule)
k = max(freq.values())

if k <= (N + 1) / 2:
    print("YES")
else:
    print("NO")

