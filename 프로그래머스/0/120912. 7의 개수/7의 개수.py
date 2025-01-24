def solution(array):
    answer = 0
    count = 0
    for char in array:
        answer += str(char).count("7")
    return answer