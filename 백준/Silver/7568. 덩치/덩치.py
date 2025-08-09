import sys
input = sys.stdin.readline

N = int(input())
people = []

for _ in range(N):
    size = tuple(map(int, input().split()))
    people.append(size)
    
for i in range(len(people)):
    rank = 0
    for j in range(len(people)):
        if i == j:
            continue
        else:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank += 1
        
    print(rank + 1, end=" ")
            
    