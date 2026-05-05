import sys

input = sys.stdin.readline


def comp(x):
    return (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0])


# input
N = int(input())
players = [tuple(map(int, input().split())) for _ in range(N)]

# solve
players = sorted(players, key=comp)

for b, p, q, r in players[:3]:
    print(b, end=" ")
print()
