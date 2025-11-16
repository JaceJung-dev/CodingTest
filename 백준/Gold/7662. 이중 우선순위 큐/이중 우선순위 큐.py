import heapq
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * K

    for idx in range(K):
        op, num = input().split()
        num = int(num)

        if op == "I":
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            visited[idx] = True
        else:
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    _, id = heapq.heappop(max_heap)
                    visited[id] = False
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    _, id = heapq.heappop(min_heap)
                    visited[id] = False

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if not max_heap or not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
