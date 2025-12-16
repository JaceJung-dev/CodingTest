import sys

input = sys.stdin.readline

N = int(input())
S = input().strip()

L = len(S)

if L <= 25:
    print(S)
else:
    trimmed_S = S[11:-11]
    if "." not in trimmed_S[:-1]:
        print(S[0:11] + "..." + S[-11:])
    else:
        print(S[0:9] + "......" + S[-10:])
