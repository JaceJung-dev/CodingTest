n = int(input())
for _ in range(n):
    results = input()
    total_score = 0
    score = 0
    for result in results:
        if result == "O":
            score += 1
            total_score += score
        elif result == "X":
            score = 0
    print(total_score)
    