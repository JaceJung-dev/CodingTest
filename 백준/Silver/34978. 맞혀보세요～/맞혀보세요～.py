import sys

input = sys.stdin.readline

N = int(input())
rules = {}
for _ in range(N):
    rule = list(input().split())
    x, m, y_list = rule[0], int(rule[1]), rule[2:]
    rules[x] = y_list

S = input().strip()
L = len(S)


def check(S, L):
    for i in range(L):
        x = S[i]
        if x in rules:
            if i != L - 1 and S[i + 1] not in rules[x]:
                return "no"
    return "yes"


print(check(S, L))
