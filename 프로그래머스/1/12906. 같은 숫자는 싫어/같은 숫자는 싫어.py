def solution(arr):
    answer = []
    prev = -1
    for num in arr:
        if num != prev:
            answer.append(num)
            prev = num
    return answer