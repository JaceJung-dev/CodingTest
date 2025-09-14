import sys
input = sys.stdin.readline

N = int(input())
convert = {"1/4": 1, "1/2": 2, "3/4": 3}
friends = [convert[input().strip()] for _ in range(N)]

friends.sort(reverse=True)
selected = [False] * N
count = 0

for i in range(N):
    if selected[i]:
        continue

    count += 1
    selected[i] = True
    total = friends[i]
    
    for j in range(i + 1, N):
        if not selected[j] and total + friends[j] <= 4:
            total += friends[j]
            selected[j] = True       
            if total == 4:
                break
            
print(count)
     