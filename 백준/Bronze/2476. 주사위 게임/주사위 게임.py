import sys
input = sys.stdin.readline

N = int(input())
highest_price = 0

for _ in range(N):
    dices = list(map(int, input().split()))
    dices.sort()
    
    dices_set = set(dices)
    if len(dices_set) == 1:
        price = 10000 + 1000 * dices[0]
    elif len(dices_set) == 2:
        price = 1000 + 100 * dices[1]
    elif len(dices_set) == 3:
        price = 100 * dices[2]
        
    if highest_price < price:
        highest_price = price
        
print(highest_price)