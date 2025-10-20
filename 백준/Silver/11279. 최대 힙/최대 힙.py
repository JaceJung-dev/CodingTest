import heapq, sys

input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    op = int(input())

    if op == 0:
        if heap:
            num = heapq.heappop(heap)[1]
            print(num)
        else:
            print(0)
    else:
        heapq.heappush(heap, (-op, op))