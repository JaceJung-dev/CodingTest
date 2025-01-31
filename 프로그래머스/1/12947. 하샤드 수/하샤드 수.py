def solution(x):
    answer = True
    x_char = str(x)
    x_sum = 0
    for num in x_char:
        x_sum += int(num)
    
    if x % x_sum == 0:
        answer = True
    else:
        answer = False
    return answer