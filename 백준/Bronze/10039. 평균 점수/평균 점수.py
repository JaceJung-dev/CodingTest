import sys

input = sys.stdin.readline

total_score = 0
for _ in range(5):
    score = int(input())
    
    if score < 40:
        total_score += 40
    else:
        total_score += score
        
print(total_score // 5)