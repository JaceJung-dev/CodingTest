A, B = map(int, input().split())
turns = 1

while A < 5 and B < 5:
    if turns % 2 == 1:
        B += A
    else:
        A += B
    turns += 1

if A >= 5:
    print("yj")
else:
    print("yt")
    