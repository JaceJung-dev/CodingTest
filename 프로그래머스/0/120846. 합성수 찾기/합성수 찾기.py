def divisor(number):
    count = 0
    for i in range(1, int(number**0.5)+1):
        if number % i == 0:
            count += 1
            if i != number // i:
                count += 1
    return count

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if divisor(i) >= 3:
            answer += 1
    return answer