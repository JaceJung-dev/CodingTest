import sys

input = sys.stdin.readline

N = int(input())
num = 1

while num * 2 < N:
    num *= 2
    
if num == N:
    print(num)
else:
    print(2 * (N - num))