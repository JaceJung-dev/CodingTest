import sys
input = sys.stdin.readline

R, C = map(int, input().split())
Rg, Cg, Rp, Cp = map(int, input().split())

room = [input().strip() for _ in range(R)]

count = 0
for i in range(R):
    for j in range(C):
        if room[i][j] == "P":
            count += 1
            
if count == Rp * Cp:
    print(0)
else:
    print(1)       