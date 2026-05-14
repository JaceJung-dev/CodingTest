import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dp[n][m]: S1의 n번째까지, S2의 m번째까지 까지 봤을 때 만들 수 있는 LCS

# Solution 1

# input
S1 = input().strip()
S2 = input().strip()

# solve
N, M = len(S1), len(S2)
S1 = " " + S1
S2 = " " + S2

dp = [[0] * (M + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for m in range(1, M + 1):
        if S1[n] == S2[m]:
            dp[n][m] = dp[n - 1][m - 1] + 1
        else:
            dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])

print(dp[N][M])

# Solution 2


def func(n, m):

    # base case
    if n == 0 or m == 0:
        return 0

    if dp[n][m] != -1:
        return dp[n][m]

    # recursive case
    if S1[n] == S2[m]:
        dp[n][m] = func(n - 1, m - 1) + 1
    else:
        dp[n][m] = max(func(n - 1, m), func(n, m - 1))

    return dp[n][m]


# input
S1 = input().strip()
S2 = input().strip()

# solve
N, M = len(S1), len(S2)
S1 = " " + S1
S2 = " " + S2

dp = [[-1] * (M + 1) for _ in range(N + 1)]

print(func(N, M))
