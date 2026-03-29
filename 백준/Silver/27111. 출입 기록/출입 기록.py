import sys

input = sys.stdin.readline

N = int(input())

errors = 0
records = {}
for _ in range(N):
    man, status = map(int, input().split())

    if man not in records:
        if status == 0:
            errors += 1
    else:
        if records[man] == status:
            errors += 1

    records[man] = status

for man in records:
    if records[man] == 1:
        errors += 1

print(errors)
