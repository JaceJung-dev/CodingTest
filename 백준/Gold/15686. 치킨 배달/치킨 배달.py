import sys
import itertools


def cal_dist(home_list, chick_list):
    total_dist = 0
    for home in home_list:
        min_dist = float("inf")
        for chick in chick_list:
            dist = abs(home[0] - chick[0]) + abs(home[1] - chick[1])
            if dist < min_dist:
                min_dist = dist
        total_dist += min_dist
    return total_dist


input = sys.stdin.readline


N, M = map(int, input().split())
home_list, chick_list = [], []
for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            home_list.append((i, j + 1))
        elif row[j] == 2:
            chick_list.append((i, j + 1))


candidate_list = list(itertools.combinations(chick_list, M))

min_dist = float("inf")
for candidate in candidate_list:
    dist = cal_dist(home_list, candidate)
    if dist < min_dist:
        min_dist = dist

print(min_dist)
