def solution(order):
    answer = 0
    a_menu, b_menu = [], []
   	
    a_menu = ["iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"]
    b_menu = ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]
    
    for menu in order:
        if menu in a_menu:
            answer += 4500
        elif menu in b_menu:
            answer += 5000
    return answer