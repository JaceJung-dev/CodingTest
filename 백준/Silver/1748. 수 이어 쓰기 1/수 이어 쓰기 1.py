import sys
input = sys.stdin.readline

N = int(input())
count = 0
start = 1
digit = 1

while True:
    end = start * 10 - 1
    
    if N <= end:
        count += (N - start + 1) * digit
        break
    
    count += (end - start + 1) * digit
    digit += 1
    start *= 10
    
print(count)