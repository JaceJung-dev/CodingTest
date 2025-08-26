def solution(s):
    answer = ''
    num_list = list(map(int, s.split()))
    answer = f"{min(num_list)} {max(num_list)}"
    return answer