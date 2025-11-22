import math
import sys

input = sys.stdin.readline


direction = 0
numer = 1
denom = 1

m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())

    direction += c
    numer *= b
    denom *= a

    g = math.gcd(numer, denom)
    numer //= g
    denom //= g

if direction % 2 == 0:
    print(0, numer // denom)
else:
    print(1, numer // denom)
