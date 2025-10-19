import sys
from collections import deque

sys.setrecursionlimit(10**6)  # 재귀 DFS 깊이 설정
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    start_node, end_node = map(int, input().split())
    graph[start_node].append(end_node)
    graph[end_node].append(start_node)

for i in range(1, N + 1):
    graph[i].sort()


def recursive_dfs(graph, cur_node, visited):
    visited[cur_node] = True
    print(cur_node, end=" ")

    for adjacent_node in graph[cur_node]:
        if not visited[adjacent_node]:
            recursive_dfs(graph, adjacent_node, visited)


def stack_dfs(graph, start_node):
    visited = [False] * (N + 1)

    stack = [start_node]

    order = []

    while stack:
        cur = stack.pop()
        if visited[cur] == True:
            continue

        visited[cur] = True
        order.append(cur)

        for adjacent_node in reversed(graph[cur]):
            if not visited[adjacent_node]:
                stack.append(adjacent_node)

    return order


def bfs(graph, start_node):
    visited = [False] * (N + 1)

    queue = deque([start_node])
    visited[start_node] = True

    order = []

    while queue:
        cur = queue.popleft()
        order.append(cur)

        for adjacent_node in graph[cur]:
            if not visited[adjacent_node]:
                queue.append(adjacent_node)
                visited[adjacent_node] = True

    return order


# recursive_dfs(graph, V, visited)
# print()

dfs_res = stack_dfs(graph, V)
bfs_res = bfs(graph, V)

print(*dfs_res)
print(*bfs_res)
