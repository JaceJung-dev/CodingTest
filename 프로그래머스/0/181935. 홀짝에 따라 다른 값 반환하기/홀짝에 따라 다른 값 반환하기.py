def solution(n):
    answer = 0
    if n % 2 == 1:
        answer = sum([num for num in range(1, n + 1) if num % 2 == 1])
    else:
        answer = sum([num ** 2 for num in range(1, n + 1) if num % 2 == 0])
    return answer