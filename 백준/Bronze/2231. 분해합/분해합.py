N = int(input())

constructor = 0
for num in range(1, N + 1):
    each_sum = sum(map(int, str(num)))
    total = num + each_sum
    
    if total == N:
        constructor = num
        break
        
print(constructor)

      