import sys

input = sys.stdin.readline

N = int(input())
players = [tuple(map(int, input().split())) for _ in range(N)]

players.sort(key=lambda x: ((x[1] * x[2] * x[3]), x[1] + x[2] + x[3], x[0]))

for i in range(3):
    print(players[i][0], end=" ")
print()
