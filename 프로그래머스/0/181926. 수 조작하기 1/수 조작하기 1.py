def solution(n, control):
    answer = n
    reference = {'w' : 1, 's' : -1, 'd': 10, 'a' : -10}
    for char in control:
        answer += reference[char]
    return answer