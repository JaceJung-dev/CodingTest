import sys

input = sys.stdin.readline

C, K = map(int, input().split())

n = 10**K
price = ((C + n // 2) // n) * n

print(price)
