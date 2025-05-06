def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
N = int(input())

num_list = list(map(int, input().split()))
count = 0
for num in num_list:
    if num == 1:
        continue
        
    if is_prime_num(num):
        count += 1
    
print(count)


