import sys
input = sys.stdin.readline

def get_gcd(n, m):
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i

n, m = map(int, input().split(":"))

gcd = get_gcd(n, m)

print(f"{n//gcd}:{m//gcd}")