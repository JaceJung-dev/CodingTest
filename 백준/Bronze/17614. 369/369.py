import sys

input = sys.stdin.readline

N = int(input())

count = 0
for num in range(1, N + 1):
    while num > 0:
        tmp = num % 10
        if tmp == 3 or tmp == 6 or tmp == 9:
            count += 1
        num //= 10

print(count)
