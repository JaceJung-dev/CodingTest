import sys

input = sys.stdin.readline

num_list = []
N = int(input())
for _ in range(N):
    num = int(input())
    num_list.append(num)
num_list.sort(reverse=True)

for num in num_list:
    print(num)
