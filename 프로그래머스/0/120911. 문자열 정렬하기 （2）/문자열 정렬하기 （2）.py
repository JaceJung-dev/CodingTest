def solution(my_string):
    str_list = [char.lower() for char in my_string]
    answer = "".join(sorted(str_list))
    return answer