import sys

input = sys.stdin.readline

R, C = map(int, input().split())
pasture = [input().rstrip() for _ in range(R)]

count = 0
clump = [0] * C
for i in range(R):
    row = pasture[i]
    prev = "."
    for j in range(len(row)):
        if prev == "#" and row[j] == "#":
            clump[j] = 1
            prev = "#"
            continue

        if row[j] == "#" and clump[j] == 0:
            clump[j] = 1
            count += 1
        elif row[j] == "." and clump[j] == 1:
            clump[j] = 0

        prev = row[j]

print(count)
