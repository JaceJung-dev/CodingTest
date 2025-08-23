import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

N = int(input())
num_list = list(map(int, input().split()))

n, d = 0, 1
for num in num_list:
    d *= num
for num in num_list:
    n += d // num
    
g = gcd(n, d)

print(f"{d // g}/{n // g}")
