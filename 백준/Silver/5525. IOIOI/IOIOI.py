import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

pn = "IO" * N + "I"
count = 0

for i in range(len(S)):
    if S[i:].startswith(pn):
        count += 1

print(count)