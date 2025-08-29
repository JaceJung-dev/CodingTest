import sys
input = sys.stdin.readline

N, M = map(int, input().split())
requests = [int(input()) for _ in range(M)]
requests.sort()
count = 0
for r in requests:
    if N - r < 0:
        break
    else:
        N -= r
        count += 1
        
print(count)

    