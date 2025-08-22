import sys
input = sys.stdin.readline

N = int(input())
num_list = [0] * 10000

for _ in range(N):
    num = int(input())
    num_list[num - 1] += 1
    
for i, v in enumerate(num_list):
    for _ in range(v):
        print(i + 1)