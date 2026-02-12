import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())
N = int(input())
top_score = 0
for _ in range(N):
    score = 0
    for _ in range(3):
        n_a, n_b, n_c = map(int, input().split())
        score += A * n_a + B * n_b + C * n_c
    top_score = max(top_score, score)

print(top_score)
