import sys
from itertools import permutations

input = sys.stdin.readline


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


S = input().strip()
count = 0

for perm in permutations(S):
    for i in range(len(S) - 1):
        if perm[i] == perm[i + 1]:
            break
    else:
        count += 1

for i in range(ord("a"), ord("z") + 1):
    count //= fact(S.count(chr(i)))

print(count)
