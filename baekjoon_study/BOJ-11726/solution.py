import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# Solution 1


def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2

    for _ in range(2, n):
        a, b = b, (a + b) % 10007

    return b


# input
N = int(input())

# solve
print(func(N))

# Solution 2

# input
N = int(input())

# solve
dp = [0] * (N + 2)
dp[1], dp[2] = 1, 2

for n in range(3, N + 1):
    dp[n] = (dp[n - 1] + dp[n - 2]) % 10007

print(dp[N])


# Solution 3


def func(n):

    # base case
    if n == 1 or n == 2:
        return n

    if dp[n] != -1:
        return dp[n]

    # recursive case
    dp[n] = (func(n - 1) + func(n - 2)) % 10007

    return dp[n]


# input
N = int(input())

# solve
dp = [-1] * (N + 1)

print(func(N))
