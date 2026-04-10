import sys

input = sys.stdin.readline

def fibo(n):
    global arr
    
    if arr[n] != -1:
        return arr[n]
    
    arr[n] = fibo(n - 1) + fibo(n - 2)
    
    return arr[n]

N = int(input())
arr = [-1] * (N + 2)
arr[0], arr[1] = 0, 1

print(fibo(N))