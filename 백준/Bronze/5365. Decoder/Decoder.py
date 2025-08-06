import sys
input = sys.stdin.readline

n = int(input())
coded_msg = input().rstrip().split()
prev = 1
decoded_msg = ""

for i in range(n):
    cur = len(coded_msg[i])
    if cur >= prev:
        decoded_msg += coded_msg[i][prev - 1]
    else:
        decoded_msg += " "      
    prev = cur
    
print(decoded_msg)