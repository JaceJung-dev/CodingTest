def solution(s):
    answer = ''
    l = len(s)
    mid = l // 2
    if l % 2 == 1:
        answer = s[mid]
    else:
        answer = s[mid-1: mid + 1]
    return answer