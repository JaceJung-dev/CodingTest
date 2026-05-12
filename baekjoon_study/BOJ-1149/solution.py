import sys

input = sys.stdin.readline

# dp[n][c] : n번째 집에서 c색으로 칠했을 때, 들어간 비용의 최솟값
# dp[n][0] = min(dp[n - 1][1], dp[n - 1][2]) + matrix[n][0]
# dp[n][1] = min(dp[n - 1][0], dp[n - 1][2]) + matrix[n][1]
# dp[n][2] = min(dp[n - 1][0], dp[n - 1][1]) + matrix[n][2]

# input
N = int(input())
matrix = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

# solve
dp = [[0, 0, 0] for _ in range(N + 1)]

for n in range(1, N + 1):
    dp[n][0] = min(dp[n - 1][1], dp[n - 1][2]) + matrix[n][0]
    dp[n][1] = min(dp[n - 1][0], dp[n - 1][2]) + matrix[n][1]
    dp[n][2] = min(dp[n - 1][0], dp[n - 1][1]) + matrix[n][2]

print(min(dp[N]))
