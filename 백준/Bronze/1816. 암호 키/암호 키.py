import sys

input = sys.stdin.readline

CUTOFF = 10 ** 6
N = int(input())
for _ in range(N):
    S = int(input())

    for i in range(2, CUTOFF + 1):
        if S % i == 0:
            print("NO")
            break
    else:
        print("YES")
