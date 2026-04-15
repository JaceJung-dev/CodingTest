import sys

input = sys.stdin.readline


def get_idx(arr, num):
    cur = -1
    step = len(arr)

    while step != 0:
        while (cur + step < len(arr)) and arr[cur + step] <= num:
            cur += step
        step //= 2

    return cur


N, H = map(int, input().split())
floor, ceiling = [], []

for i in range(N):
    obs = int(input())
    if i % 2 == 0:
        floor.append(obs)
    else:
        ceiling.append(H - obs + 1)

floor.sort()
ceiling.sort()

len_floor = len(floor)
len_ceiling = len(ceiling)

min_broke = 10**6
min_pos = 0

for height in range(1, H + 1):
    cnt_floor = (N // 2) - (get_idx(floor, height - 1) + 1)
    cnt_ceiling = get_idx(ceiling, height) + 1

    if min_broke == cnt_floor + cnt_ceiling:
        min_pos += 1

    if min_broke > cnt_floor + cnt_ceiling:
        min_broke = cnt_floor + cnt_ceiling
        min_pos = 1

print(min_broke, min_pos)
