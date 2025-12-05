import sys

input = sys.stdin.readline

N = int(input())
count = 0

for a in range(3, N, 3):
    for b in range(3, N - a, 3):
        c = N - a - b
        if c >= 3:
            count += 1

print(count)
