import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    visited = [False for _ in range(10001)]
    queue = deque()
    queue.append([A, ""])
    visited[A] = True

    while queue:
        num, command = queue.popleft()

        if num == B:
            print(command)
            break

        d = num * 2 % 10000
        if not visited[d]:
            queue.append([d, command + "D"])
            visited[d] = True

        s = (num - 1) % 10000
        if not visited[s]:
            queue.append([s, command + "S"])
            visited[s] = True

        l = num // 1000 + (num % 1000) * 10
        if not visited[l]:
            queue.append([l, command + "L"])
            visited[l] = True

        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            queue.append([r, command + "R"])
            visited[r] = True
