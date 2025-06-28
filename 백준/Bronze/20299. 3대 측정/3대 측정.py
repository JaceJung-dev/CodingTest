import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())
vip_members = []
vip_count = 0

for _ in range(N):
    team = list(map(int, input().split()))
    
    if sum(team) >= K and all(member >= L for member in team):
        vip_count += 1
        vip_members.extend(team)

print(vip_count)
print(*vip_members)