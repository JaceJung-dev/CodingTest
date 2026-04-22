import heapq
import sys

input = sys.stdin.readline

INF = 10 ** 8


def dijkstra(snode):
    dist = [INF] * (N + 1)
    dist[snode] = 0

    heap = []
    heapq.heappush(heap, (0, snode))

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        for nxt_node, nxt_dist in adj_list[cur_node]:
            temp_dist = cur_dist + nxt_dist
            if temp_dist < dist[nxt_node]:
                dist[nxt_node] = temp_dist
                heapq.heappush(heap, (temp_dist, nxt_node))

    return dist


N, M, X = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    adj_list[s].append((e, w))  # (node, weight)


go_dists = [0] * (N + 1)

for i in range(1, N + 1):
    dists = dijkstra(i)
    go_dists[i] = dists[X]

back_dists = dijkstra(X)

total_dist = [0] * (N + 1)
for i in range(1, N + 1):
    total_dist[i] = go_dists[i] + back_dists[i]

print(max(total_dist))
