N = int(input())
S = input()

status = 1
area = 0

for select in S:
    if select == "W":
        area += 1
    elif select == "P":
        if area == 0:
            status *= -1
        elif area == 1:
            status *= 0

if area >= 2:
    if status == 1:
        print(5)
    elif status == -1:
        print(1)
    elif status == 0:
        print(6)
else:
    print(0)