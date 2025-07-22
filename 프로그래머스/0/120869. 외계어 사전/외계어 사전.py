def solution(spell, dic):
    answer = 2
    for word in dic:
        is_possible = True
        for char in spell:
            if word.count(char) != 1:
                is_possible = False
                break
            
        if is_possible:
            answer = 1
            break
    return answer