import sys

input = sys.stdin.readline

areas = []
N = int(input())
for _ in range(N):
    h, w = map(int, input().split())
    area = h * w
    areas.append(area)

print(max(areas))
