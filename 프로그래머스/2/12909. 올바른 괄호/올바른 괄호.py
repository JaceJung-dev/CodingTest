def solution(s):
    answer = True
    
    opened, closed = 0, 0
    
    for char in s:
        if char == "(":
            opened += 1
        else:
            closed += 1
    
        if opened < closed:
            answer = False
            break
    
    if opened != closed:
        answer = False
        
    return answer