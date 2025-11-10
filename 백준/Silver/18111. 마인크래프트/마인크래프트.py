import sys

input = sys.stdin.readline


N, M, B = map(int, input().split())
min_h, max_h = 256, 0
blocks = [0] * 257

min_time = float("inf")
opt_h = -1

for _ in range(N):
    row = list(map(int, input().split()))
    for i in range(M):
        h = row[i]
        blocks[h] += 1
        min_h = min(min_h, h)
        max_h = max(max_h, h)

for height in range(min_h, max_h + 1):
    remove = 0
    add = 0
    
    for h in range(height + 1, max_h + 1):
        if blocks[h]:
            remove += (h - height) * blocks[h] 
    for h in range(min_h, height):
        if blocks[h]:
            add += (height - h) * blocks[h]

    if B + remove < add:
        continue

    time = 2 * remove + add
    if time < min_time or (time == min_time and height > opt_h):
        min_time = time
        opt_h = height

print(min_time, opt_h)