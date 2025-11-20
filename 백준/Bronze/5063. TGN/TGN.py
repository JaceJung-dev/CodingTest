import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    r, e, c = map(int, input().split())
    profit = e - c

    if profit > r:
        print("advertise")
    elif profit < r:
        print("do not advertise")
    else:
        print("does not matter")
