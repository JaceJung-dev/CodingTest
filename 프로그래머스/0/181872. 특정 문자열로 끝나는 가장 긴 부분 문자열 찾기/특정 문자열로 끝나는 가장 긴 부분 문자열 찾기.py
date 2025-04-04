def solution(myString, pat):
    answer = ''
    i = myString.rfind(pat)
    
    answer = myString[:i + len(pat)]
    return answer