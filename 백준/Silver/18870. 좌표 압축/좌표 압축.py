import sys

input = sys.stdin.readline

N = int(input())
coordinates = list(map(int, input().split()))

unique_sorted = sorted(set(coordinates))

rank = {value: idx for idx, value in enumerate(unique_sorted)}

for x in coordinates:
    print(rank[x], end=" ")