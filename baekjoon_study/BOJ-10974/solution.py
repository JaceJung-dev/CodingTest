import sys
from itertools import permutations

input = sys.stdin.readline


# Solution 1
def permutation(level):

    # base case
    if level == N:
        print(*selections)
        return

    # recursive case
    for i in range(1, N):
        if check[i]:
            continue

        check[i] = True
        selections.append(i)
        permutation(level + 1)

        selections.pop()
        check[i] = False


# input
N = int(input())

# solve
selections = []
check = [False for _ in range(N)]

permutation(0)

# Solution 2

# input
N = int(input())

# solve
for permutation in permutations(range(1, N + 1), N):
    print("".join(map(str, permutation)))
