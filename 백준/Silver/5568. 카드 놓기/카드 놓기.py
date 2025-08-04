import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
k = int(input())

cards = [input().strip() for _ in range(n)]

result = set()

for comb in permutations(cards, k):
    result.add("".join(comb))
    
print(len(result))