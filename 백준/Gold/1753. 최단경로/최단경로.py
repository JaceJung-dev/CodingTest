import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
adj_list = [[] for _ in range(V + 1)]
dist = [float("inf")] * (V + 1)
dist[K] = 0

for _ in range(E):
    s, e, d = map(int, input().split())
    adj_list[s].append((e, d))

heap = []
heapq.heappush(heap, (0, K))  # (dist, node)

while heap:
    cur_dist, cur_node = heapq.heappop(heap)

    if cur_dist > dist[cur_node]:
        continue

    for adj_node, adj_dist in adj_list[cur_node]:
        temp_dist = cur_dist + adj_dist

        if temp_dist < dist[adj_node]:
            dist[adj_node] = temp_dist
            heapq.heappush(heap, (temp_dist, adj_node))

for num in dist[1:]:
    print(num if not num == float("inf") else "INF")
