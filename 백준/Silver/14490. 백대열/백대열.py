import sys
input = sys.stdin.readline

def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n, m = map(int, input().split(":"))
gcd = get_gcd(n, m)
print(f"{n//gcd}:{m//gcd}")