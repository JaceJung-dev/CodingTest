import sys

input = sys.stdin.readline

N = int(input())
dp = [0] + [10**9] * N

squares = []
j = 1
while j * j <= N:
    squares.append(j * j)
    j += 1

for i in range(1, N + 1):
    for s in squares:
        if s > i:
            break

        if dp[i - s] + 1 < dp[i]:
            dp[i] = dp[i - s] + 1

print(dp[N])
