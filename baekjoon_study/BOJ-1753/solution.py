import heapq
import sys

input = sys.stdin.readline

INF = 10**12

# input
V, E = map(int, input().split())
K = int(input())
adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    s, e, d = map(int, input().split())
    adj_list[s].append((e, d))

# solve
dist = [INF] * (V + 1)
dist[K] = 0

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

for d in dist[1:]:
    print(d if not d == INF else "INF")
