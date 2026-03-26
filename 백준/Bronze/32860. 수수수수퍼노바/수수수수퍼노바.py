import sys

input = sys.stdin.readline

N, M = map(int, input().split())

if M <= 26:
    suffix = chr(ord("A") + M - 1)
else:
    tmp = M - 27
    first = tmp // 26
    second = tmp % 26
    suffix = chr(ord("a") + first) + chr(ord("a") + second)

print(f"SN {N}{suffix}")

