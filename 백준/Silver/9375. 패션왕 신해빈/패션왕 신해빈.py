import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    clothes_dict = defaultdict(list)

    for _ in range(N):
        clothes, category = input().split()
        clothes_dict[category].append(clothes)

    cases = 1
    for category, clothes in clothes_dict.items():
        cases *= len(clothes) + 1
        
    print(cases - 1)
