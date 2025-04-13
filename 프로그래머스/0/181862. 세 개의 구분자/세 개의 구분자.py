def solution(myStr):
    answer = []
    char_list = ["a", "b", "c"]
    
    for char in char_list:
        myStr = myStr.replace(char, "|")
    newStr = myStr.split("|")
    
    for element in newStr:
        if element != "":
            answer.append(element)
    
    if answer == []:
        answer = ["EMPTY"]
    return answer