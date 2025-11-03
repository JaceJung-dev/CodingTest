import sys

input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
current_end = -1

for start, end in meetings:
    if start >= current_end:
        count += 1
        current_end = end
        
print(count)