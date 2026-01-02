import sys

input = sys.stdin.readline

A, B = map(int, input().split())

low, high = min(A, B), max(A, B)

total = (low + high) * (high - low + 1) // 2

print(total)