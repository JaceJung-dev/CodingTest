while True:
    sides = list(map(int, input().split()))

    if sides == [0, 0, 0]:
        break
    else:
        sides.sort()
        a, b, c = sides[0], sides[1], sides[2]
        if a**2 + b**2 == c**2:
            print("right")
        else:
            print("wrong")
                