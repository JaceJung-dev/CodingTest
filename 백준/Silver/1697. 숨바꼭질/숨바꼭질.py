import sys
from collections import deque

input = sys.stdin.readline

MAX = 10**5
N, M = map(int, input().split())
visited = [False] * (MAX + 1)


queue = deque()
queue.append((0, N))
visited[N] = True

while queue:
    time, pos = queue.popleft()

    if pos == M:
        print(time)
        exit()

    for nxt_pos in [pos - 1, pos + 1, pos * 2]:
        if (0 <= nxt_pos <= MAX) and (not visited[nxt_pos]):
            queue.append((time + 1, nxt_pos))
            visited[nxt_pos] = True
