import heapq, sys

input = sys.stdin.readline

heap = []

n = int(input())

for _ in range(n):
    operator = int(input())

    if operator == 0:
        if heap:
            min_num = heapq.heappop(heap)
        else:
            min_num = 0
        print(min_num)
    else:
        heapq.heappush(heap, operator)
