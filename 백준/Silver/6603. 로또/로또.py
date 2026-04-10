import sys

input = sys.stdin.readline


def combination(index, level):

    if level == 6:
        print(*selection)
        return

    for i in range(index, K):
        selection.append(S[i])
        combination(i + 1, level + 1)
        selection.pop()


while True:
    inputs = list(map(int, input().split()))

    if inputs == [0]:
        break

    K, S = inputs[0], inputs[1:]

    selection = []
    combination(0, 0)
    print()
