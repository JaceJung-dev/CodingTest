import sys
input = sys.stdin.readline


def permutation(level):
    global N, M
    if level == M:
        print(*choose)
        return

    prev = -1

    for i in range(N):
        if check[i]:
            continue
        if nums[i] == prev:
            continue

        check[i] = True
        choose.append(nums[i])
        prev = nums[i]

        permutation(level + 1)

        choose.pop()
        check[i] = False


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
choose = []
check = [False] * N

permutation(0)
