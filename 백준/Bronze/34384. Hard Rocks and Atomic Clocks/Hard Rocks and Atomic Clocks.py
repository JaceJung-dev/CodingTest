import sys

input = sys.stdin.readline

time = int(input())

target_time = ((time // 3600) + 1) * 3600 + 59

time_left = target_time - time

min_left = time_left // 60

print(min_left)
