import sys

input = sys.stdin.readline

N, M = map(int, input().split())

if N >= M:
    print(0)
else:
    answer = 1
    for i in range(2, N + 1):
        answer = (answer * i) % M
    print(answer)

