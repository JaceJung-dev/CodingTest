import sys
input = sys.stdin.readline

N = int(input())
N_set = set(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for m in M_list:
    if m in N_set:
        print(1)
    else:
        print(0)
    