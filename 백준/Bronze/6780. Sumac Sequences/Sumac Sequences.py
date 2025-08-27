import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

length = 1
while b >= 0:
    length += 1
    a, b = b, a - b
    
print(length)