import sys

input = sys.stdin.readline

arr = ["" for _ in range(13)]
arr[0] = "-"

for i in range(1, 13):
    arr[i] = arr[i - 1] + " " * 3 ** (i - 1) + arr[i - 1]
    
while True:
    try:
        N = int(input())
        print(arr[N])
    except:
        break