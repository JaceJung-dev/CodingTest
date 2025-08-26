import sys
input = sys.stdin.readline

N = int(input())

i = 0
num = 666
is_done = False
ans = 0
while not is_done:
    if "666" in str(num):
        ans = num
        i += 1
        num += 1
    else:
        num += 1
        
    if i == N:
        is_done = True
        
print(ans)