import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num2name = [None] * (N + 1)
name2num = {}

for i in range(1, N + 1):
    pokemon = input().strip()
    num2name[i] = pokemon
    name2num[pokemon] = i

answer = []
for _ in range(M):
    query = input().strip()

    if query.isdigit():
        answer.append(num2name[int(query)])
    else:
        answer.append(str(name2num[query]))

print("\n".join(answer))
