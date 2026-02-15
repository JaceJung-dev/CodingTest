import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    num = 1
    while count < N:
        if arr[count] == num:
            num += 1
            continue
        else:
            count += 1
            num += 1

    print(num - 1)
