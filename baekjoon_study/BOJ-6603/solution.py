import sys
from itertools import combinations

input = sys.stdin.readline


# 직접 구현
def combination(index, level):

    if level == 6:
        print(*selection)
        return

    for i in range(index, K):
        selection.append(S[i])
        combination(i + 1, level + 1)
        selection.pop()


while True:
    I = list(map(int, input().split()))

    K, S = I[0], I[1:]

    if K == 0:
        break

    selection = []
    combination(0, 0)
    print()

# 라이브러리 사용
while True:
    I = list(map(int, input().split()))

    K, S = I[0], I[1:]

    if K == 0:
        break

    for comb in combinations(S, 6):
        print(*comb)

    print()
