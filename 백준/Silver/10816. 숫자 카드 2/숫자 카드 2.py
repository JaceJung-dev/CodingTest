import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
query = list(map(int, input().split()))

count = Counter(cards)

for q in query:
    print(count[q], end=" ")
