import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
L = list(map(int, input().split()))
C = input().split()

is_found = False
p1, p2 = 0, 0
for i in range(N):
    for j in range(i+1, N):
        if C[i] != C[j] and abs(X[i] - X[j]) <= L[i] + L[j]:
            is_found = True
            p1, p2 = i + 1, j + 1
    if is_found:
        break

if is_found:
    print("YES")
    print(p1, p2)
else:
    print("NO")
            