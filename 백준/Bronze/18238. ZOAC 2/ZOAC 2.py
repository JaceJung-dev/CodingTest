import sys

input = sys.stdin.readline

chars = input().strip()

cur = "A"
move = 0
for char in chars:
    gap = abs(ord(char) - ord(cur))
    move += min(gap, 26 - gap)
    cur = char

print(move)
