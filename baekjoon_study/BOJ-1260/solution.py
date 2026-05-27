import sys
from collections import deque

input = sys.stdin.readline


def solve_dfs(node):
    if visited[node]:
        return

    print(node, end=" ")

    visited[node] = True

    for adj_node in adj_list[node]:
        solve_dfs(adj_node)


def solve_stack_dfs(snode):
    stack = []
    stack.append(snode)

    while stack:
        cur_node = stack.pop()
        if visited[cur_node]:
            continue

        visited[cur_node] = True
        print(cur_node, end=" ")

        for adj_node in reversed(adj_list[cur_node]):
            if not visited[adj_node]:
                stack.append(adj_node)


def solve_bfs(snode):
    queue = deque()
    queue.append(snode)
    visited[snode] = True

    while queue:
        cur_node = queue.popleft()
        print(cur_node, end=" ")

        for adj_node in adj_list[cur_node]:
            if not visited[adj_node]:
                queue.append(adj_node)
                visited[adj_node] = True


# input
N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

# solve
for _ in range(M):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

for n in range(1, N + 1):
    adj_list[n].sort()


# Solution 1 (dfs)
visited = [False] * (N + 1)
solve_dfs(V)
print()

# Solution 2 (dfs)
visited = [False] * (N + 1)
solve_stack_dfs(V)
print()

# Solution (bfs)
visited = [False] * (N + 1)
solve_bfs(V)
print()
