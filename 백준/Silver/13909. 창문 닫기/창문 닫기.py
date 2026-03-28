import sys

input = sys.stdin.readline

N = int(input())

left, right = 0, N
ans = 0

while left <= right:
    mid = (left + right) // 2

    if mid * mid <= N:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
