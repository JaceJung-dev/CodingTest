import sys
input = sys.stdin.readline

T = int(input())
input()
print(T)
for _ in range(T):
    N = int(input())
    seq = list(map(int, input().split()))
    input()
    if N >= 2:
        seq[-1], seq[-2] = seq[-2], seq[-1]
        
    print()
    print(N)
    print(" ".join(map(str, seq)))
