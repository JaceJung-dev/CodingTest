import heapq
import sys


input = sys.stdin.readline


n = int(input())
requests = [tuple(map(int, input().split())) for _ in range(n)]

requests.sort(key=lambda x: x[1])

heap = []

for request in requests:
    pay, day = request

    if len(heap) < day:
        heapq.heappush(heap, pay)
    elif len(heap) == day and heap[0] < pay:
        heapq.heappop(heap)
        heapq.heappush(heap, pay)

print(sum(heap))