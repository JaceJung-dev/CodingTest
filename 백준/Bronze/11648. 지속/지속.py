import sys

input = sys.stdin.readline

N = input().strip()

count = 0
while len(N) > 1:
    acc = 1
    for num in N:
        acc *= int(num)

    count += 1
    N = str(acc)

print(count)
