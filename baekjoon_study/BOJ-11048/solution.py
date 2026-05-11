import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# Solution 1

# input
N, M = map(int, input().split())
matrix = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# solve
dp = [[0] * (M + 1) for _ in range((N + 1))]

for n in range(1, N + 1):
    for m in range(1, M + 1):
        dp[n][m] = max(dp[n - 1][m], dp[n - 1][m - 1], dp[n][m - 1]) + matrix[n][m]


print(dp[N][M])


# Solution 2
def func(n, m):
    global dp

    if dp[n][m] != -1:
        return dp[n][m]

    dp[n][m] = max(func(n - 1, m), func(n - 1, m - 1), func(n, m - 1)) + matrix[n][m]

    return dp[n][m]


# input
N, M = map(int, input().split())
matrix = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# solve
dp = [[-1] * (M + 1) for _ in range(N + 1)]

for j in range(M + 1):
    dp[0][j] = 0

for i in range(N + 1):
    dp[i][0] = 0

print(func(N, M))
