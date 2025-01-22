def solution(i, j, k):
    num_list = [str(num) for num in range(i, j+1)]
    num_char = "".join(num_list)
    return num_char.count(str(k))