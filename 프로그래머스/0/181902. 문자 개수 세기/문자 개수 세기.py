def solution(my_string):
    answer = [0] * 52
    for char in my_string:
        if char.isupper():
            idx = ord(char) - ord("A")
            answer[idx] += 1
        else:
            idx = ord(char) - ord("a") + 26
            answer[idx] += 1
    return answer