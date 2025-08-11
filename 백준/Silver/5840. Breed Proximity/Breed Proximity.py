import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cows = {}
max_id = -1

for i in range(N):
    cow = int(input())
    if cow in cows and i - cows[cow] <= K:
        if cow > max_id:
            max_id = cow
            
    cows[cow] = i
    
print(max_id)
    
