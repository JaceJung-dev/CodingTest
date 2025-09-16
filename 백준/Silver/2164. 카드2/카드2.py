import sys
from collections import deque


input = sys.stdin.readline

N = int(input())
queue = deque([i for i in range(1, N + 1)])

while len(queue) > 1:
    queue.popleft()
    return_card = queue.popleft()
    queue.append(return_card)

print(queue[0])