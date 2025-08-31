import sys
from functools import lru_cache


input = sys.stdin.readline

@lru_cache(maxsize=None)
def w(a, b, c):
    while True:
        if a <= 0 or b <= 0 or c <= 0:
            return 1
    
        if a > 20 or b > 20 or c > 20:
            a, b, c = 20, 20, 20

        if a < b and b < c:
            return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    
    ans = w(a, b, c)
    print(f"w({a}, {b}, {c}) = {ans}")