import sys
input = sys.stdin.readline

def get_num(x, y):
    if x == y:
        k = x // 2
        if x % 2 == 0:
            return 4 * k
        else:
            return 4 * k + 1
    elif x >= 2 and y == x - 2:
        k = x // 2
        if x % 2 == 0:
            return 4 * k - 2
        else:
            return 4 * k - 1
    else:
        return "No Number"
    
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    num = get_num(x, y)
    print(num)
    
    