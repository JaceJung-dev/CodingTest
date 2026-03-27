import sys

input = sys.stdin.readline

LIMIT = 10 ** 6
is_prime = [True] * (LIMIT + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(LIMIT ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, LIMIT + 1, i):
            is_prime[j] = False

primes = [num for num in range(2, LIMIT + 1) if is_prime[num]]

N = int(input())
for _ in range(N):
    S = int(input())

    for prime in primes:
        if S % prime == 0:
            print("NO")
            break
    else:
        print("YES")
