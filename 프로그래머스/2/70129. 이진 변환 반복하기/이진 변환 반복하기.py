def cvt_binary(num):
    temp = ""
    while num > 0:
        left = num % 2
        temp += str(left)
        num = num // 2
    return temp[::-1]

def solution(s):
    answer = []
    zero_count = 0
    cvt_count = 0
    while s != "1":
        temp = ""
        for char in s:
            if char == "0":
                zero_count += 1
                continue
            else:
                temp += char
        s = cvt_binary(len(temp))
        cvt_count += 1
    answer = [cvt_count, zero_count]
    return answer