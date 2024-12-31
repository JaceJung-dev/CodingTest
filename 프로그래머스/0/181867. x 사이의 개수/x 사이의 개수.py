def solution(myString):
    split_arr = myString.split('x')
    answer = [len(char) for char in split_arr]
    return answer