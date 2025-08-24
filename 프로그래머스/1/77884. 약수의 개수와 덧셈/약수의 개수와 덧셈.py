def num_of_cd(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)
    

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        num_cd = num_of_cd(num)
        if num_cd % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer