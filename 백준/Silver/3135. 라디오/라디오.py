import sys
input = sys.stdin.readline

cur_frequency, next_frequency = map(int, input().split())
N = int(input())
favorite = [int(input()) for _ in range(N)]

cur_gap = abs(next_frequency - cur_frequency)

favorite_to_next_gap = [abs(next_frequency - frequency) for frequency in favorite]
min_gap = min(favorite_to_next_gap) + 1

if min_gap < cur_gap:
    print(min_gap)
else:
    print(cur_gap)
