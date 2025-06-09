num = int(input())

step = 1

while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = 3 * num + 1
    
    step += 1
    
print(step)