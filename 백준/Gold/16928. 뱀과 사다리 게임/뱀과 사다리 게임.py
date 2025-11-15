import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

jumps = {}
for _ in range(N + M):
    s, e = map(int, input().split())
    jumps[s] = e

visited = [False] * 101
queue = deque([])
queue.append((1, 0))
visited[1] = True

while queue:
    curr_pos, count = queue.popleft()

    if curr_pos == 100:
        print(count)
        break

    for dice in range(1, 7):
        next_pos = curr_pos + dice
        if next_pos > 100:
            continue

        if next_pos in jumps:
            next_pos = jumps[next_pos]

        if not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, count + 1))
