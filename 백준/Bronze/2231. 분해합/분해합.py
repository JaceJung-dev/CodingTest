N = int(input())

constructor = 0
for num in range(1, N + 1):
    each_sum = 0
    for each_num in str(num):
        each_sum += int(each_num)
    total = num + each_sum
    
    if total == N:
        constructor = num
        break
        
print(constructor)

      