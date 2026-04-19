import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

parent = [0] * (N + 1)

queue = deque()
queue.append(1)
parent[1] = -1

while queue:
    cur_node = queue.popleft()

    for adj_node in adj_list[cur_node]:
        if parent[adj_node] == 0:
            parent[adj_node] = cur_node
            queue.append(adj_node)

for i in range(2, N + 1):
    print(parent[i])
