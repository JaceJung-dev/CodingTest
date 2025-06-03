N = int(input())

total = 1
for num in range(2, N + 1):
    total *= num
    
print(total)