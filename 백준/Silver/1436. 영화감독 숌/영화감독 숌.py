import sys
input = sys.stdin.readline

N = int(input())
i, num = 0, 666

while True:
    if "666" in str(num):
        i += 1
        if i == N:
            print(num)
            break
    num += 1