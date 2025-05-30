M = int(input())
N = int(input())

sqr_list = []
for i in range(1, 101):
    sqr_num = i * i
    if M <= sqr_num <= N:
        sqr_list.append(sqr_num)
        
if sqr_list:
    print(sum(sqr_list))
    print(min(sqr_list))
else:
    print(-1)