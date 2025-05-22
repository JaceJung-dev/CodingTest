L, P = map(int,input().split())
news_list = list(map(int,input().split()))

real_num = L * P

for num in news_list:
    print(num - real_num, end=" ")