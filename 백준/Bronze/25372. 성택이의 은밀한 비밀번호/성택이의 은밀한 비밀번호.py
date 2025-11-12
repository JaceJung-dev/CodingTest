import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    candidate = input().strip()

    if 6 <= len(candidate) <= 9:
        print("yes")
    else:
        print("no")

