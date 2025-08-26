import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    

T = int(input())
for _ in range(T):
    A, B, X = map(int, input().split())
    
    G = gcd(A, B)
    print(X // G)