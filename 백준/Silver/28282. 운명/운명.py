import sys
from collections import Counter

input = sys.stdin.readline

X, K = map(int, input().split())
socks_color = list(map(int, input().split()))

left = socks_color[:X]
right = socks_color[X:]


l_color_count = Counter(left)
r_color_count = Counter(right)

total = X * X

same_color = 0
for color, l_count in l_color_count.items():
    same_color += l_count * r_color_count.get(color, 0)

print(total - same_color)
