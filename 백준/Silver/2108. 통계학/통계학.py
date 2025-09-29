import math
import sys
from collections import Counter


def round_up(num):
    return int(math.floor(num + 0.5) if num >= 0 else math.ceil(math.ceil(num - 0.5)))


def cal_mode(num_list):
    counter = Counter(num_list)
    max_count = max(counter.values())

    max_list = [n for n, c in counter.items() if c == max_count]
    max_list.sort()

    return max_list[0] if len(max_list) == 1 else max_list[1]


input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]
length = len(num_list)
num_list.sort()

mean = round_up((sum(num_list) / length))
median = num_list[length // 2]
mode = cal_mode(num_list)
num_range = num_list[-1] - num_list[0]

print(mean)
print(median)
print(mode)
print(num_range)
