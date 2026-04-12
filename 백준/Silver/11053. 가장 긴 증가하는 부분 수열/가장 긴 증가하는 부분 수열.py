import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums = [0] + nums

dp = [0] * (N + 1)

for n in range(1, N + 1):
    best = 0
    for i in range(1, n):
        if nums[n] > nums[i]:
            best = max(best, dp[i])
    dp[n] = best + 1

print(max(dp))
