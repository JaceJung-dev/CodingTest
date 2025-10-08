import sys
from collections import deque


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    target = int(input())
    fin_combination = set()
    queue = deque([[1], [2], [3]])

    while queue:
        cur = queue.popleft()

        if sum(cur) < target:
            queue.append(cur + [1])
            queue.append(cur + [2])
            queue.append(cur + [3])
        elif sum(cur) == target:
            fin_combination.add(tuple(cur))

    print(len(fin_combination))