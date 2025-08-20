import sys
input = sys.stdin.readline

isbn = input().rstrip()

total = 0

for i, v in enumerate(isbn[:-1]):
    if v == "*":
        if i % 2 == 0:
            weight = 1
        else:
            weight = 3
        continue
        
    if i % 2 == 0:
        total += int(v)
    else:
        total += 3 * int(v)

for i in range(10):
    if (total + int(isbn[-1]) + weight * i) % 10 == 0:
        print(i)