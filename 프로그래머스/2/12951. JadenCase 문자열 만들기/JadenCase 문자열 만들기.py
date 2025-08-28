def solution(s):
    answer = ''
    is_first = True
    for char in s:
        if char == " ":
            answer += char
            is_first = True
        else:
            if is_first:
                answer += char.upper()
                is_first = False
            else:
                answer += char.lower()
    return answer