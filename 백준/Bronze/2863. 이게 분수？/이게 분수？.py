import sys

input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())

scores = []

scores.append(((A / C + B / D), 0))
scores.append(((C / D + A / B), 1))
scores.append(((D / B + C / A), 2))
scores.append(((B / A + D / C), 3))


scores.sort(key=lambda x: -x[0])

print(scores[0][1])
