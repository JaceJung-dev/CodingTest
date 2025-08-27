N = int(input())
count = 0

while N > 1:
    count += N // 5
    N //= 5
    
print(count)