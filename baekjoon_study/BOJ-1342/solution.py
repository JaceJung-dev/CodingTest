import sys
from itertools import permutations

input = sys.stdin.readline


# Solution 1


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


# input
S = input().strip()

# solve
count = 0
for perm in permutations(S):
    for i in range(len(S) - 1):
        if perm[i] == perm[i + 1]:
            break
    else:
        count += 1

for char in range(ord("a"), ord("z") + 1):
    count //= fact(S.count(chr(char)))

print(count)


# Solution 2


def func(level):
    global S, chars, counter, selections, count
    if level == len(S):
        count += 1
        return

    for char in chars:
        if counter[char] == 0:
            continue

        if (not selections) or selections[-1] != char:
            selections.append(char)
            counter[char] -= 1
            func(level + 1)
            selections.pop()
            counter[char] += 1


# input
S = input().strip()

# solve
chars = set()
counter = dict()
selections = []

for char in S:
    chars.add(char)
    counter[char] = counter.get(char, 0) + 1

count = 0
func(0)

print(count)
