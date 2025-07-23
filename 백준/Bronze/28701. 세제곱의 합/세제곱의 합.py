N = int(input())

sum_num = 0
cubed_sum = 0
for num in range(1, N + 1):
    sum_num += num
    cubed_sum += num ** 3
    
sum_squared = (sum_num) ** 2

print(sum_num)
print(sum_squared)
print(cubed_sum)
