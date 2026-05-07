import sys
from itertools import combinations

input = sys.stdin.readline

# Solution 1


def partial_comb(level):
    global N, S, nums, selections, count

    # base case
    if level == N:
        if selections and sum(selections) == S:
            count += 1
        return

    # recursive case
    # choose current element
    selections.append(nums[level])
    partial_comb(level + 1)
    selections.pop()

    # not choose current element
    partial_comb(level + 1)


N, S = map(int, input().split())
nums = list(map(int, input().split()))
selections = []
count = 0

partial_comb(0)
print(count)

# Solution 2


def partial_comb2(level):
    global N, S, nums, cur_sum, count

    # base case
    if level == N:
        if cur_sum == S:
            count += 1
        return

    # recursive case
    # choose current element
    cur_sum += nums[level]
    partial_comb2(level + 1)
    cur_sum -= nums[level]

    # not choose current element
    partial_comb2(level + 1)


N, S = map(int, input().split())
nums = list(map(int, input().split()))
cur_sum = 0
count = 0

partial_comb2(0)

if S == 0:
    count -= 1

print(count)


# Solution 3

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(1, N + 1):
    for candidate in combinations(nums, i):
        if sum(candidate) == S:
            count += 1

print(count)
