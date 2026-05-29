import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def solve_dfs(snode):
    global visited, count

    if visited[snode]:
        return

    visited[snode] = True
    count += 1

    for adj_node in adj_list[snode]:
        solve_dfs(adj_node)


def solve_bfs(node):
    global visited, count
    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue:
        cur_node = queue.popleft()

        count += 1

        for adj_node in adj_list[cur_node]:
            if not visited[adj_node]:
                queue.append(adj_node)
                visited[adj_node] = True


N = int(input())
M = int(input())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    c1, c2 = map(int, input().split())
    adj_list[c1].append(c2)
    adj_list[c2].append(c1)

# Solution 1
visited = [False] * (N + 1)
count = 0
solve_dfs(1)
print(count - 1)

# Solution 2
visited = [False] * (N + 1)
count = 0
solve_bfs(1)
print(count - 1)
