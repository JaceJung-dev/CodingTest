def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a    

def solution(n, m):
    g = gcd(n, m)
    l = n * m // g
    return [g, l]