num_list = list(map(int,input().split()))

code = 0
final_code = 0
for num in num_list:
    code += num ** 2

print(code % 10)
