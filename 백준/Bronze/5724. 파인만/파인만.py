import sys

input = sys.stdin.readline

while True:
    N = int(input())

    if N == 0:
        break
    count = 0
    for i in range(1, N + 1):
        count += i * i

    print(count)
