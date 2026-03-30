import sys

input = sys.stdin.readline

n, b = map(int, input().split())

cutoff = 2 ** (b + 1) - 1

if n <= cutoff:
    print("yes")
else:
    print("no")
