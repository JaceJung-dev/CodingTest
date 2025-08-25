import sys
input = sys.stdin.readline

def get_prime_list(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return [i for i, v in enumerate(is_prime) if v]

def factorize(num, prime_list):
    factors = []
    for p in prime_list:
        if p ** 2 > num:
            break
        
        while num % p ==0:
            factors.append(p)
            num //= p
    if num > 1:
        factors.append(num)
    
    return factors


N = int(input())
num_list = [int(input()) for _ in range(N)]

primes = get_prime_list(46340) # (2^31 - 1) ** 0.5

for num in num_list:
    factors = factorize(num, primes)
    if len(factors) == 1 and factors[0] == num:
        print(f"{num}: prime")
    else:
        print(f"{num}: {' '.join(map(str, factors))}")

