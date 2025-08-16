import sys
input = sys.stdin.readline
    
T = int(input())
numbers = list(map(int, input().split()))

max_num = max(numbers)
num_sum = [0] * (max_num + 1)

for div_num in range(1, max_num // 2 + 1):
    for mul_num in range(div_num * 2, max_num + 1, div_num):
        num_sum[mul_num] += div_num

for num in numbers:
    if num_sum[num] > num:
        print("abundant")
    elif num_sum[num] < num:
        print("deficient")
    else:
        print("perfect")