def solution(brown, yellow):
    answer = []
    def get_divisors(num):
        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append((i, num // i))
                
        return divisors
    
    divisors = get_divisors(yellow)
    
    for a, b in divisors:
        if 2 * a + 2 * b + 4 == brown:
            answer = [b + 2, a + 2]
    return answer