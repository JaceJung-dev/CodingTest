import sys
input = sys.stdin.readline

n, w = map(int, input().split())

prices = []
for _ in range(n):
    price = int(input())
    prices.append(price)
    
prev_price = prices[0]
coin = 0
for price in prices:
    if price > prev_price:
        coin += w // prev_price
        w %= prev_price
    elif price < prev_price:
        w += (coin * prev_price)
        coin = 0
    prev_price = price

w += (coin * prices[-1])
print(w)
