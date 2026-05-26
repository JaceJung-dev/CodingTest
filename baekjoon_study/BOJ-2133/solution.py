import sys

input = sys.stdin.readline

# Solution 1-1

# input
N = int(input())

# solve
dp = [0] * 31
dp[0] = 1

for n in range(2, 31, 2):
    dp[n] = 3 * dp[n - 2]
    for i in range(n - 4, -1, -2):
        dp[n] += 2 * dp[i]

print(dp[N])

# Solution 1-2


def func(n):

    # base case
    if n % 2 == 1:
        return 0

    if dp[n] != -1:
        return dp[n]

    # recursive case
    dp[n] = 3 * func(n - 2)

    for i in range(n - 4, -1, -2):
        dp[n] += 2 * func(i)

    return dp[n]


# input
N = int(input())

# solve
dp = [-1] * 31
dp[0] = 1

print(func(N))

# Solution 2-1

# input
N = int(input())

# solve
dp = [[0] * 3 for _ in range(31)]
dp[1][1] = 2
dp[2][0] = 2
dp[2][2] = 3

for n in range(3, 31):
    dp[n][0] = dp[n - 1][1]
    dp[n][1] = 2 * dp[n - 1][2] + dp[n - 1][0]
    dp[n][2] = dp[n][0] + dp[n - 2][2]

print(dp[N][2])


# Solution 2-2


def func(n, k):

    # base case
    if n <= 0:
        return 0
    if dp[n][k] != -1:
        return dp[n][k]

    # recursive case
    if k == 0:
        dp[n][k] = func(n - 1, 1)
    if k == 1:
        dp[n][1] = 2 * func(n - 1, 2) + func(n - 1, 0)
    if k == 2:
        dp[n][2] = func(n, 0) + func(n - 2, 2)

    return dp[n][k]


# input
N = int(input())

# solve
dp = [[-1] * 3 for _ in range(31)]
dp[1][1] = 2
dp[2][0] = 2
dp[2][2] = 3

print(func(N, 2))
