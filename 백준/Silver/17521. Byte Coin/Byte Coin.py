import sys

input = sys.stdin.readline

n, w = map(int, input().split())

prices = []
for _ in range(n):
    prices.append(int(input()))

coin = 0
for i in range(n-1):
    if prices[i] < prices[i + 1]:
        coin += w // prices[i]
        w %= prices[i]
    elif prices[i] > prices[i + 1]:
        w += (coin * prices[i])
        coin = 0

w += (coin * prices[-1])
print(w)