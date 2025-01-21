def solution(n):
    answer = 0
    divisor_list = []
    for i in range(1, int(n**(0.5)) +1):
        if n % i == 0:
            divisor_list.append(i)
            if n // i != i:
                divisor_list.append(n // i)
    answer = sum(divisor_list)
    return answer