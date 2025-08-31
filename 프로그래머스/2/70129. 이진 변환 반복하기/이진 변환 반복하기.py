def solution(s):
    answer = []
    zero_count = 0
    cvt_count = 0
    while s != "1":
        cvt_count += 1
        one_count = s.count("1")
        zero_count += len(s) - one_count
        s = bin(one_count)[2:]
    answer = [cvt_count, zero_count]
    return answer