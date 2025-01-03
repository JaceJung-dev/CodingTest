def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def solution(numer1, denom1, numer2, denom2):
    new_denom = denom1 * denom2
    new_numer = numer1 * denom2 + numer2 * denom1
    
    gcd_value = gcd(new_numer, new_denom)
    
    answer = [new_numer / gcd_value , new_denom / gcd_value]
    return answer