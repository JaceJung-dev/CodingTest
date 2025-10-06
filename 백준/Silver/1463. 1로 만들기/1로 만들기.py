import sys

input = sys.stdin.readline

dp = [0] * 1000001

dp[1] = 0

for i in range(2, 1000001):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i - 1], dp[i // 3], dp[i // 2]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i - 1], dp[i // 3]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i - 1], dp[i // 2]) + 1
    else:
        dp[i] = dp[i - 1] + 1

N = int(input())

print(dp[N])
