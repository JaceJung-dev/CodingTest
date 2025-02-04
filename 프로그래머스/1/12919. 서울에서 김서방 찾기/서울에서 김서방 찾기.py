def solution(seoul):
    answer = ''
    for i, v in enumerate(seoul):
        if v == "Kim":
            answer = f"김서방은 {i}에 있다"
    return answer