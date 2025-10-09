import sys
from collections import deque

input = sys.stdin.readline

computers = int(input())
network_num = int(input())

networks = [[] for _ in range(computers + 1)]

for _ in range(network_num):
    cur, nex = map(int, input().split())
    networks[cur].append(nex)
    networks[nex].append(cur)

infected = [False] * (computers + 1)
infected[1] = True

count = 0
queue = deque([1])

while queue:
    cur = queue.popleft()

    for nex in networks[cur]:
        if not infected[nex]:
            infected[nex] = True
            count += 1
            queue.append(nex)

print(count)
