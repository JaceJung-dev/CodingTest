import sys

input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())

if a + b <= N:
    one_count = a + b
else:
    one_count = N - (a + b - N)

max_value = 0
for i in range(one_count):
    max_value += 2 ** (N - 1 - i)

print(max_value)
