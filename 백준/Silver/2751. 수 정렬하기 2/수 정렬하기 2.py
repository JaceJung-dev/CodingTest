import sys
input = sys.stdin.readline

N = int(input())
ordered_list = [0] * 2000001
for _ in range(N):
    i = int(input())
    ordered_list[i+ 1000000] = 1
print("\n".join(str(i) for i in range(-1000000,1000001,1) if ordered_list[i+1000000]))