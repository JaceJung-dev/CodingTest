import sys

input = sys.stdin.readline

N = int(input())

length = ((N - 1) // 9) + 1

if length % 2 == 0 and N % 2 == 1:
    length += 1
print(length)
