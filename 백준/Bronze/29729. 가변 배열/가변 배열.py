import sys
input = sys.stdin.readline

S, N, M = map(int, input().split())

current = 0
for _ in range(N + M):
    action = int(input())
    
    if action == 1:
        if S <= current:
            current += 1
            S *= 2
        else:
            current += 1
    else:
        current -= 1
        
print(S)
        