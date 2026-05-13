import sys

input = sys.stdin.readline

# Solution 1

# input
N = int(input())
nums = [0] + list(map(int, input().split()))

# solve
dp = [0] * (N + 1)

for n in range(1, N + 1):
    best = 0
    for i in range(1, n):
        if nums[n] > nums[i]:
            best = max(best, dp[i])
    dp[n] = best + 1

print(max(dp))


# Solution 2
def func(n):
    if dp[n] != -1:
        return dp[n]

    best = 0
    for i in range(1, n):
        if nums[n] > nums[i]:
            best = max(best, func(i))

    dp[n] = best + 1

    return dp[n]


# input
N = int(input())
nums = [0] + list(map(int, input().split()))

# solve
dp = [-1] * (N + 1)
dp[1] = 1

for i in range(1, N + 1):
    func(i)

print(max(dp[1:]))
