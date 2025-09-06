import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
ingredient = list(map(int, input().split()))
ingredient.sort()

count = 0
i, j = 0, N-1

while i < j:
    total = ingredient[i] + ingredient[j]
    if total == M:
        count += 1
        i += 1
        j -= 1
    elif total > M:
        j -= 1
    elif total < M:
        i += 1
        
print(count)