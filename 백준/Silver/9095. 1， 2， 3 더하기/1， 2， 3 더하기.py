import sys


input = sys.stdin.readline

T = int(input())
dp = [0] * 13
dp[1] = 1  # 1
dp[2] = 2  # 1+1, 2
dp[3] = 4  # 1+1+1, 1+2, 2+1, 3

for i in range(4, 13):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(T):
    target = int(input())
    print(dp[target])
