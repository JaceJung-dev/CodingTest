import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

len_s1, len_s2 = len(s1), len(s2)

s1 = " " + s1
s2 = " " + s2

dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

for i in range(1, len_s1 + 1):
    for j in range(1, len_s2 + 1):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len_s1][len_s2])
