import sys
from math import ceil

input = sys.stdin.readline

N = int(input())

count = 0
for a in range(ceil(N / 3), ceil(N / 2)):
    count += a - ceil((N - a) / 2) + 1

print(count)
