import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())
vip_count = 0
vip_member = []

for _ in range(N):
    team = list(map(int, input().split()))
    
    if sum(team) < K:
        continue
    
    is_disqulified = False
    for person in team:
        if person < L:
            is_disqulified = True
    
    if is_disqulified:
        continue
    
    vip_count += 1
    vip_member += team
    
print(vip_count)
for person in vip_member:
    print(person, end=" ")
    
    