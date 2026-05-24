import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# Solution 1

MAX = 10001
INF = 10**12

# input
N, M = map(int, input().split())
mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

# solve
dp = [[0] * MAX for _ in range(N + 1)]

for n in range(1, N + 1):
    for c in range(0, MAX):
        dp[n][c] = dp[n - 1][c]
        if c - costs[n] >= 0:
            dp[n][c] = max(dp[n][c], dp[n - 1][c - costs[n]] + mems[n])

ans = INF
for c in range(0, MAX):
    if dp[N][c] >= M:
        ans = min(ans, c)

print(ans)

# Solution 2

MAX = 10001
INF = 10**12


def func(n, c):

    # base case
    if n == 0:
        return 0
    if dp[n][c] != -1:
        return dp[n][c]

    # recursive case
    dp[n][c] = func(n - 1, c)
    if c - costs[n] >= 0:
        dp[n][c] = max(dp[n][c], func(n - 1, c - costs[n]) + mems[n])

    return dp[n][c]


# input
N, M = map(int, input().split())
mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

# solve
dp = [[-1] * MAX for _ in range(N + 1)]

# 파라매트릭 서치도 가능
ans = INF
for c in range(0, MAX):
    if func(N, c) >= M:
        ans = min(ans, c)

print(ans)
