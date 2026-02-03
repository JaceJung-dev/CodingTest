import sys

input = sys.stdin.readline

def push(b1, b2, b3, lost):
    if b3 and b2 and b1:
        lost += 1
        b3 = False
    
    if b2 and b1:
        b3 = True
        b1 = False

    if b1:
        b2 = True
        b1 = False

    b1 = True
    return b1, b2, b3, lost


N = int(input())
throws = list(map(int, input().split()))

b1, b2, b3 = False, False, False
ball = 0
lost = 0

for throw in throws:
    if throw == 3:
        if b3:
            lost += 1
        b3, b2, b1 = b2, b1, False

        ball += 1
        if ball == 4:
            b1, b2, b3, lost = push(b1, b2, b3, lost)
            ball = 0

    elif throw == 1:
        ball += 1
        if ball == 4:
            b1, b2, b3, lost = push(b1, b2, b3, lost)
            ball = 0

    else:
        b1, b2, b3, lost = push(b1, b2, b3, lost)
        ball = 0

print(lost)
