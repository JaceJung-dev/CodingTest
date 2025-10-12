import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = [tuple(map(int, input().split())) for _ in range(K)]

    visited = [[False] * N for _ in range(M)]
    queue = deque()
    count = 0

    for j in range(M):
        for i in range(N):
            if (j, i) in cabbages and not visited[j][i]:
                queue.append((j, i))
                visited[j][i] = True

                while queue:
                    y, x = queue.popleft()

                    for dy, dx in dirs:
                        new_y, new_x = y + dy, x + dx

                        if (new_y < 0 or new_y > M - 1) or (new_x < 0 or new_x > N - 1):
                            continue

                        if (new_y, new_x) in cabbages and not visited[new_y][new_x]:
                            queue.append((new_y, new_x))
                            visited[new_y][new_x] = True

                count += 1

    print(count)
