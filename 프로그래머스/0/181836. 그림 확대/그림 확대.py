def solution(picture, k):
    answer = []
    for line in picture:
       	temp = ""
        for char in line:
            temp += char * k
        for _ in range(k):
            answer.append(temp)
    return answer