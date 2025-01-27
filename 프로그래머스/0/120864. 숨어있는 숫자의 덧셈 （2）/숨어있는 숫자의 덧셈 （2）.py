def solution(my_string):
    answer = 0
    temp_num = ""
    for char in my_string:
        if char.isdigit():
            temp_num += char
        else:
            if temp_num:
                answer += int(temp_num)
                temp_num = ""

    if temp_num:
        answer += int(temp_num)

    return answer