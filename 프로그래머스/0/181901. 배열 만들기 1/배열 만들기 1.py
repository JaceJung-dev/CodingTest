def solution(n, k):
    answer = [num for num in range(1, n + 1) if num % k == 0]
    return answer