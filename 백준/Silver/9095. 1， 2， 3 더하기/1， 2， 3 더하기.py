import sys
from collections import deque


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    target = int(input())
    queue = deque([0])
    count = 0

    while queue:
        cur = queue.popleft()

        if cur == target:
            count += 1
        elif cur < target:
            queue.append(cur + 1)
            queue.append(cur + 2)
            queue.append(cur + 3)

    print(count)
