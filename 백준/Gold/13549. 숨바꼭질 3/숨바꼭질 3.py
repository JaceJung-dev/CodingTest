import heapq
import sys

input = sys.stdin.readline

INF = 10**12
MAX = 10**5

N, M = map(int, input().split())

time = [INF] * (MAX + 1)

heap = []
time[N] = 0
heapq.heappush(heap, (0, N))

while heap:
    cur_time, cur_node = heapq.heappop(heap)

    nxts = [
        (cur_time + 1, cur_node + 1),
        (cur_time + 1, cur_node - 1),
        (cur_time, cur_node * 2),
    ]

    for nxt_time, nxt_node in nxts:
        if 0 <= nxt_node <= MAX:
            if nxt_time < time[nxt_node]:
                time[nxt_node] = nxt_time
                heapq.heappush(heap, (nxt_time, nxt_node))

print(time[M])
