N = int(input())
S = input()

lever = False
area = 0
drift = False

for select in S:
    if select == "W":
        area += 1
    elif select == "P":
        if area == 0:
            lever = not lever
        elif area == 1:
            drift = True
            
if area < 2:
    print(0)
else:
    if drift:
        print(6)
    else:
        if lever:
            print(1)
        else:
            print(5)

