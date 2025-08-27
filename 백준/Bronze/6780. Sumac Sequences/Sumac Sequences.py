import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
l = 2
while a - b >= 0:
    a, b = b, a - b
    l += 1
print(l)