import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

update_list = num_list[:]

for i in range(N):
    for j in range(i):
        if num_list[j] < num_list[i]:
            update_list[i] = max(update_list[i], num_list[i] + update_list[j])
            
print(max(update_list))