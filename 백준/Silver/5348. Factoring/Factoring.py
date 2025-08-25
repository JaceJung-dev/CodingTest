import sys
input = sys.stdin.readline

def prime_factorization(n):
    prime = []
    for i in range(2, n + 1):
        while True:
            if n % i == 0:
                prime.append(i)
                n //= i
            else:
                break
                
    return prime
            

N = int(input())
for _ in range(N):
    num = int(input())
    prime = prime_factorization(num)
    
    if len(prime) == 1:
        print(f"{num}: prime")
    else:
        print(f"{num}:", end=" ")
        print(*prime)