N = int(input())
M = int(input())

sqr_list = []
for num in range(N, M+1):
    sqr_num = num ** 0.5
    if sqr_num.is_integer():
        sqr_list.append(num)
        
if sqr_list:       
    print(sum(sqr_list))
    print(min(sqr_list))
else:
    print(-1)