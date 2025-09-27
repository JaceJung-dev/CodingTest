import sys


input = sys.stdin.readline

N = int(input())

if N == 0:
    print(0)
else:
    scores = [int(input()) for _ in range(N)]
    scores.sort()

    cutoff = (N * 15 + 50) // 100
    final_score = sum(scores[cutoff : N - cutoff]) / (N - 2 * cutoff)

    print(int(final_score + 0.5))
