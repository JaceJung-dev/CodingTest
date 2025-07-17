import sys
input = sys.stdin.readline

N = int(input())

min_x, max_x = float("inf"), float("-inf")
min_y, max_y = float("inf"), float("-inf")

for _ in range(N):
    x, y = map(int, input().split())
    if x < min_x:
        min_x = x
    elif x > max_x:
        max_x = x
    
    if y < min_y:
        min_y = y
    elif y > max_y:
        max_y = y

print(max(max_x - min_x, max_y - min_y) ** 2)