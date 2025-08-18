import sys
from collections import defaultdict

input = sys.stdin.readline

cows = set()
deg = defaultdict(int)
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
comfortable_count = 0


def update_neighbor_change(p):
    before = deg[p]
    delta = 0
    if before == 3:
        delta -= 1
    deg[p] = before + 1
    
    if deg[p] == 3:
        delta += 1
    
    return delta


N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    
    cows.add((x, y))
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if (nx, ny) in cows:
            comfortable_count += update_neighbor_change((nx, ny))
            comfortable_count += update_neighbor_change((x, y))
            
    print(comfortable_count)