def solution(myString):
    answer = ''
    for char in myString:
        if ord(char) < 108:
            answer += 'l'
        else:
            answer += char
            
    return answer