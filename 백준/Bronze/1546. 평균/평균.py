N = int(input())
scores = list(map(int,input().split()))

max_score = max(scores)

modified_mean = (sum(scores) / len(scores)) / max_score * 100

print(round(modified_mean, 6))