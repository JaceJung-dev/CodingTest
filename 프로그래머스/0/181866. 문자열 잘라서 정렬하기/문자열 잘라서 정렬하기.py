def solution(myString):
    s_list = myString.split("x")
    answer = sorted([char for char in s_list if char])
    return answer