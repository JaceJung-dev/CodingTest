import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())

over = 0
hives = []
for _ in range(N):
    hive = int(input())
    over += hive // M
    remain = hive % M
    if remain > 0:
        hives.append(remain)

honey = 0
if over >= K:
    honey = M * K
else:
    times = K - over
    hives.sort(reverse=True)
    times = min(times, len(hives))
    honey = M * over + sum(hives[:times])

print(honey)