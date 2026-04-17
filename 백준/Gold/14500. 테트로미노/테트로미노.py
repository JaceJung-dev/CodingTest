import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
visited = [[False] * M for _ in range(N)]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(N):
    board.append(list(map(int, input().split())))

max_sum = 0


def dfs(x, y, cur_sum, level):
    global max_sum

    if level == 3:
        max_sum = max(max_sum, cur_sum)
        return

    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
            continue

        if level == 1:
            visited[nx][ny] = True
            dfs(x, y, cur_sum + board[nx][ny], level + 1)
            visited[nx][ny] = False

        visited[nx][ny] = True
        dfs(nx, ny, cur_sum + board[nx][ny], level + 1)
        visited[nx][ny] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 0)
        visited[i][j] = False

print(max_sum)
