def solution(quiz):
    answer = []
    for q in quiz:
        equation = q.split("=")
        print(equation[0], equation[1])
        if eval(equation[0]) == int(equation[1].strip()):
            answer.append("O")
        else:
            answer.append("X")
    return answer