total = int(input())
price_sum = 0
for _ in range(9):
    price = int(input())
    price_sum += price
    
print(total - price_sum)