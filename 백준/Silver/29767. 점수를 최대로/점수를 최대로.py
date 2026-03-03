import sys

input = sys.stdin.readline

N, K = map(int, input().split())
classes = list(map(int, input().split()))

accum_scores = []
accum_score = 0
for score in classes:
    accum_score += score
    accum_scores.append(accum_score)

accum_scores.sort(reverse=True)

print(sum(accum_scores[:K]))
