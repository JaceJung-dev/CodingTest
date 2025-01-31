def solution(s):
    char = s.lower()
    p_count = char.count("p")
    y_count = char.count("y")
    
    if p_count == y_count:
        return True
    else:
        return False