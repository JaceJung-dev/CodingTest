import sys


input = sys.stdin.readline


N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]

min_count = 64

for sj in range(N - 7):
    for si in range(M - 7):
        count = 0
        start = board[sj][si]
        
        for j in range(8):
            for i in range(8):
                cur = board[sj + j][si + i]
                if (i + j) % 2 == 0 and cur != start:
                    count += 1
                if (i + j) % 2 == 1 and cur == start:
                    count += 1
                    
        min_count = min(min_count, count, 64 - count)
        
print(min_count)