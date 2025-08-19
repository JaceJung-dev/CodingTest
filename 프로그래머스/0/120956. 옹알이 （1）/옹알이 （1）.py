def solution(babbling):
    answer = 0
    pron_list = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for pron in pron_list:
            word = word.replace(pron, " ")
        
        word = word.replace(" ", "")
        
        if not word:
            answer += 1
            
    return answer