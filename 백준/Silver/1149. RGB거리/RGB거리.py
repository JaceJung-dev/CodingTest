import sys

input = sys.stdin.readline

N = int(input())
cost = [[0, 0, 0]]
cost += [list(map(int, input().split())) for _ in range(N)]

dp = [[-1, -1, -1] for _ in range(N + 1)]

for i in range(3):
    dp[1][i] = cost[1][i]

for i in range(2, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

print(min(dp[N]))
