import sys

input = sys.stdin.readline

N, M = map(int, input().split())

data = {}
ans = []

for _ in range(N):
    site, pw = input().split()
    data[site] = pw

for _ in range(M):
    query = input().strip()
    ans.append(data[query])

print("\n".join(ans))
