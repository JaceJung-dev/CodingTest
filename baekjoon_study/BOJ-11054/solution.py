import sys

input = sys.stdin.readline

# Solution 1

# input
N = int(input())
nums = [0] + list(map(int, input().split()))

# solve
dp1 = [0] * (N + 1)
dp2 = [0] * (N + 1)
dp1[1], dp2[N] = 1, 1

for n in range(1, N + 1):
    dp1[n] = 1
    for i in range(1, n):
        if nums[n] > nums[i]:
            dp1[n] = max(dp1[n], dp1[i] + 1)

for n in range(N - 1, 0, -1):
    dp2[n] = 1
    for i in range(N, n, -1):
        if nums[n] > nums[i]:
            dp2[n] = max(dp2[n], dp2[i] + 1)

ans = 0
for i in range(1, N + 1):
    ans = max(ans, dp1[i] + dp2[i] - 1)

print(ans)


# Solution 2
def func1(n):

    # base case
    if dp1[n] != -1:
        return dp1[n]

    # recursive case
    dp1[n] = 1
    for i in range(1, n):
        if nums[n] > nums[i]:
            dp1[n] = max(dp1[n], func1(i) + 1)

    return dp1[n]


def func2(n):

    # base case
    if dp2[n] != -1:
        return dp2[n]

    # recursive case
    dp2[n] = 1
    for i in range(N, n, -1):
        if nums[n] > nums[i]:
            dp2[n] = max(dp2[n], func2(i) + 1)

    return dp2[n]


# input
N = int(input())
nums = [0] + list(map(int, input().split()))

# solve
dp1 = [-1] * (N + 1)
dp2 = [-1] * (N + 1)
dp1[1], dp2[N] = 1, 1

ans = 0
for i in range(1, N + 1):
    ans = max(ans, func1(i) + func2(i) - 1)

print(ans)
