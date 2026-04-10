import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
infos = [input().split() for _ in range(N)]

count = 0
for candidate in permutations(range(1, 10), 3):
    is_ok = True

    for num, st, bl in infos:
        cur_st, cur_bl = 0, 0

        for i in range(3):
            if str(candidate[i]) == num[i]:
                cur_st += 1
            elif str(candidate[i]) in num:
                cur_bl += 1

        if cur_st != int(st) or cur_bl != int(bl):
            is_ok = False
            break

    if is_ok:
        count += 1

print(count)
