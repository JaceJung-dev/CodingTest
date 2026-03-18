import sys

input = sys.stdin.readline

S = input().rstrip('\n')

if len(S) >= 2 and S[0] == '"' and S[-1] == '"' and len(S[1:-1]) > 0:
    print(S[1:-1])
else:
    print("CE")