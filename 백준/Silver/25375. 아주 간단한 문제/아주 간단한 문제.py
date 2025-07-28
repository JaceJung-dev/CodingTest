import sys
input = sys.stdin.readline

def is_coprime(x, y):
    for i in range(2, min(x, y)):
        if x % i and y % i == 0:
            return False
    return True

N = int(input())
for _ in range(N):
    a, b = map(int,input().split())
    
    if b % a != 0:
        print(0)
        continue
        
    else:
        num = b // a
        for i in range(num // 2):
            x, y = i, num - i
            
            if is_coprime(x, y):
                print(1)
                break
        else:
            print(0)
                       