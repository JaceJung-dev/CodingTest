import sys

input = sys.stdin.readline

W, H, N = map(int, input().split())
spots = [tuple(map(int, input().split())) for _ in range(N)]

total_move = 0
for i in range(N - 1):
    x_gap = spots[i + 1][0] - spots[i][0]
    y_gap = spots[i + 1][1] - spots[i][1]

    if x_gap * y_gap > 0:
        move = max(abs(x_gap), abs(y_gap))
    elif x_gap == 0:
        move = abs(y_gap)
    elif y_gap == 0:
        move = abs(x_gap)
    else:
        move = abs(x_gap) + abs(y_gap)

    total_move += move

print(total_move)
