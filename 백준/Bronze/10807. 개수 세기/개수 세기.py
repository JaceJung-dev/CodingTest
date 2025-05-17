N = int(input())
num_list = map(int,input().split())
check_num = int(input())

count = 0
for num in num_list:
    if num == check_num:
        count += 1

print(count)