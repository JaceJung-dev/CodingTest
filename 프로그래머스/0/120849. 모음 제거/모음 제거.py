def solution(my_string):
    answer = ''
    vowels = ['a', 'e', 'i' , 'o', 'u']
    for char in my_string:
        if char not in vowels:
            answer += char
    return answer