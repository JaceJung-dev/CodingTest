import sys

input = sys.stdin.readline

H, M, S = map(int, input().split())
Q = int(input())

time = 3600 * H + 60 * M + S
for _ in range(Q):
    query = input().strip()

    if query == "3":
        h = time // 3600
        m = (time % 3600) // 60
        s = time % 60
        print(h, m, s)
    else:
        op, sec = query.split()
        if op == "1":
            time = (time + int(sec)) % 86400
        else:
            time = (time - int(sec)) % 86400
