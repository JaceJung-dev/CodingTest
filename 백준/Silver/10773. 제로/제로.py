import sys

input = sys.stdin.readline

K = int(input())
account = []
for _ in range(K):
    num = int(input())

    if num == 0:
        account.pop()
    else:
        account.append(num)

print(sum(account))
