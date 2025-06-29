import sys
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
computers = [0] * (N + 1)
total = N

for _ in range(Q):
    query = input().split()
    if len(query) > 1:
        q, x = int(query[0]), int(query[1])
    else:
        q = int(query[0])

    if q == 1:
        if not computers[x]:
            computers[x] = 1
            total -= 1
    elif q == 2:
        if computers[x]:
            computers[x] = 0
            total += 1
    else:
        print(total)