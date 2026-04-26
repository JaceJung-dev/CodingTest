import heapq
import sys

input = sys.stdin.readline

INF = 10**8


def dijkstra(node):
    dist = [INF] * (N + 1)
    dist[node] = 0
    heap = []
    heapq.heappush(heap, (0, node))

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        
        if cur_dist > dist[cur_node]:
            continue

        for adj_node, adj_dist in adj_list[cur_node]:
            temp_dist = cur_dist + adj_dist
            if temp_dist < dist[adj_node]:
                dist[adj_node] = temp_dist
                heapq.heappush(heap, (temp_dist, adj_node))
    return dist


N = int(input())
M = int(input())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    adj_list[s].append((e, w))  # (node, weight)

for i in range(1, N + 1):
    dist = dijkstra(i)[1:]
    for num in dist:
        print(0 if num == INF else num, end=" ")
    print()
