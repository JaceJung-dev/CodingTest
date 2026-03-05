import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, word = input().split()
    n = int(n) - 1
    revised = word[:n] + word[n + 1 :]
    print(revised)
