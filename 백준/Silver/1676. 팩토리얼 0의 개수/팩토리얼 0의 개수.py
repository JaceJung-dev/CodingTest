import sys
input = sys.stdin.readline

N = int(input())

count = 0
for num in range(1, N + 1):
    while num % 5 == 0:
        count += 1
        num = num // 5
        
print(count)