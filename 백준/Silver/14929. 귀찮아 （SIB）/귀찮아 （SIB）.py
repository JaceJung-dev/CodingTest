import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_sum = sum(num_list)

total = 0

for num in num_list:
    num_sum -= num
    total += num * num_sum

print(total)
