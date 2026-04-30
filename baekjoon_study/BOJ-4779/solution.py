import sys

input = sys.stdin.readline

# solution 1
ans = ["" for _ in range(13)]
ans[0] = "-"

for i in range(1, 13):
    ans[i] = ans[i - 1] + " " * 3 ** (i - 1) + ans[i - 1]

while True:
    try:
        N = int(input())
        print(ans[N])
    except:
        break


# Solution 2
def cantor(n):
    if n == 0:
        print("-", end="")
        return

    cantor(n - 1)
    print(" " * 3 ** (n - 1), end="")
    cantor(n - 1)


while True:
    try:
        N = int(input())
        cantor(N)
        print()
    except:
        break


# Solution 3
# 문자열로 반환하는 함수로
def cantor2(n):
    if n == 0:
        return "-"

    return cantor2(n - 1) + " " * 3 ** (n - 1) + cantor2(n - 1)


while True:
    try:
        N = int(input())
        print(cantor2(N))
    except:
        break
