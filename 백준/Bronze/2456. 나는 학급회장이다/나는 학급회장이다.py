import sys

input = sys.stdin.readline

N = int(input())
total_scores = [0] * 3
total_scores_square = [0] * 3

for _ in range(N):
    scores = list(map(int, input().split()))
    for i in range(3):
        score = scores[i]
        total_scores[i] += score
        total_scores_square[i] += score * score

max_score = max(total_scores)

if total_scores.count(max_score) == 1:
    for i in range(3):
        if total_scores[i] == max_score:
            print(i + 1, max_score)

else:
    max_score_square = max(total_scores_square)
    if total_scores_square.count(max_score_square) == 1:
        idx = total_scores_square.index(max_score_square)
        print(idx + 1, max_score)
    else:
        print(0, max_score)
