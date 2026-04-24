import sys

input = sys.stdin.readline

N = int(input())
triangle = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    nums = list(map(int, input().split()))

    triangle[i] = nums

dp = [[-1] * i for i in range(0, N + 1)]
dp[1][0] = triangle[1][0]

# dp[n][a] n번째 줄 a번째 원소까지 최대합
# dp[n][a] = max(dp[n - 1][a - 1], dp[n - 1][a]) + triange[n][a]

for i in range(2, N + 1):
    for j in range(i):
        if j == 0:
            dp[i][j] = dp[i - 1][0] + triangle[i][0]
        elif j == i - 1:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

print(max(dp[N]))
