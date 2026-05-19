import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# Solution 1

# input
N = int(input())
nums = [0] + list(map(int, input().split()))

# solve
dp = [0] * (N + 1)

for n in range(1, N + 1):
    dp[n] = max(0, dp[n - 1]) + nums[n]

print(max(dp[1:]))

# Solution 2

INF = 10**12


def func(n):

    # base case
    if n == 0:
        return 0

    if dp[n] != -INF:
        return dp[n]

    # recursive case
    dp[n] = max(0, func(n - 1)) + nums[n]

    return dp[n]


# input
N = int(input())
nums = [0] + list(map(int, input().split()))

# solve
dp = [-INF] * (N + 1)

ans = -INF
for i in range(1, N + 1):
    ans = max(ans, func(i))

print(ans)
