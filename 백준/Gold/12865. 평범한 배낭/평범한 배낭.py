import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def func(n, k):
    global W, V, dp

    if n == 0 or k == 0:
        return 0

    if dp[n][k] != -1:
        return dp[n][k]

    if k >= W[n]:
        dp[n][k] = max(func(n - 1, k), func(n - 1, k - W[n]) + V[n])
    else:
        dp[n][k] = func(n - 1, k)

    return dp[n][k]


N, K = map(int, input().split())
W, V = [0], [0]

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

dp = [[-1] * (K + 1) for _ in range(N + 1)]

print(func(N, K))
