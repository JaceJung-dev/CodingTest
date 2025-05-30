A, B = map(int, input().split())

M = (B - A) / 400

P = 1 / (1 + 10 ** M)

print(P)