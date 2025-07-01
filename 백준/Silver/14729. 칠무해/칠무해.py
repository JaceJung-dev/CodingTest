import sys
input = sys.stdin.readline

N = int(input())
scores = []
for _ in range(N):
    score = float(input())
    scores.append(score)
    
scores.sort()

for score in scores[:7]:
    print(f"{score:.3f}")