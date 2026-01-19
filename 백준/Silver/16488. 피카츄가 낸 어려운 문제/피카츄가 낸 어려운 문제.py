import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# 직각삼각형, 빗변 1/2 지점, K번
print(N * N * K)