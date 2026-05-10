import sys

input = sys.stdin.readline

# input
N, M = map(int, input().split())
locations = list(map(int, input().split()))

# solve
pos = []
neg = []
for location in locations:
    if location > 0:
        pos.append(location)
    else:
        neg.append(-location)

pos = sorted(pos, reverse=True)
neg = sorted(neg, reverse=True)

dists = []

for p in pos[::M]:
    dists.append(p)

for n in neg[::M]:
    dists.append(n)

print(2 * sum(dists) - max(dists))
