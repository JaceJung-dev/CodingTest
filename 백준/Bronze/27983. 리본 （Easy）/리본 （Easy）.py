import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
L = list(map(int, input().split()))
C = input().split()

for i in range(N):
    for j in range(i + 1, N):
        if C[i] != C[j] and abs(X[i] - X[j]) <= L[i] + L[j]:
            print("YES")
            print(i + 1, j + 1)
            exit()
print("NO")
