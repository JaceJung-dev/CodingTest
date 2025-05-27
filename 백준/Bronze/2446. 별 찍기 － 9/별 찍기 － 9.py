N = int(input())

for i in range(0, N):
    print(" " * i + "*" * (2 * (N-i) - 1))
for j in range(N-2, -1, -1):
    print(" " * j + "*" * (2 * (N-j) - 1))