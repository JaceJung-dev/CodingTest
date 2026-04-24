import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(2)]

    dp = [[-1] * 3 for _ in range(N)]
    dp[0][0] = 0
    dp[0][1] = matrix[0][0]
    dp[0][2] = matrix[1][0]

    for i in range(1, N):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + matrix[0][i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + matrix[1][i]

    print(max(dp[N - 1]))
