import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    columns = [1] * M
    for _ in range(N):
        row = list(map(int, input().split()))
        for i in range(M):
            columns[i] *= row[i]

    max_value = max(columns)
    max_indexs = [i for i, v in enumerate(columns) if v == max_value]
    print(max(max_indexs) + 1)
