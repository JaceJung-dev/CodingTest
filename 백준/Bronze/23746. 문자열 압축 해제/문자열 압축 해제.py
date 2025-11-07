import sys

input = sys.stdin.readline

decode = {}
N = int(input())
for _ in range(N):
    ori, comp = input().split()
    decode[comp] = ori

compressed = input().strip()
S, E = map(int, input().split())
original_char = [decode[c] for c in compressed]

print("".join(original_char)[S-1:E])
