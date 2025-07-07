import sys
input = sys.stdin.readline

cur_frequency, next_frequency = map(int, input().split())
N = int(input())

min_gap = abs(next_frequency - cur_frequency)

for _ in range(N):
    frequency = int(input())
    min_gap = min(abs(next_frequency - frequency) + 1, min_gap)
    
print(min_gap)