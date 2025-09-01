import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

total = 0
for i in range(N + 1):
    total += sum(num_list[:i])
    
print(total)