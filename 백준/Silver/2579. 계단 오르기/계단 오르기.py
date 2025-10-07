import sys


input = sys.stdin.readline

N = int(input())
scores = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)

if N == 1:
    print(scores[1])
elif N == 2:
    print(scores[1] + scores[2])
else:
    dp[1], dp[2] = scores[1], scores[1] + scores[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 3] + scores[i - 1], dp[i - 2]) + scores[i]

    print(dp[N])
