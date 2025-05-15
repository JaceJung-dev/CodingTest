def get_gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
        
def get_prime_factor(n):
    prime_factor = []
    x = 2
    while x <= n:
        if n % x == 0:
            n //= x
            if x not in prime_factor:
                prime_factor.append(x)
        else:
            x += 1
    return prime_factor

def solution(a, b):
    gcd = get_gcd(a, b)
    a, b = int(a/gcd), int(b/gcd)
    
    prime_factor_list = get_prime_factor(b)
    
    for i in prime_factor_list:
        if i != 2 and i != 5:
            return 2
    return 1