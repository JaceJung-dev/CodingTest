import sys

N = int(sys.stdin.readline())

for _ in range(N):
    expression = sys.stdin.readline().rstrip()
    
    i = 0
    num = -1
    logical = 1
    for element in expression:
        if element == "!":
            logical *= -1
        else:
            num = element
            break
            
    if expression[-1] == "!":
        if logical == 1:
            print(1)
        else:
            print(0)
    else:
        if num == "0":
            if logical == 1:
                print(0)
            else:
                print(1)
        else:
            if logical == 1:
                print(1)
            else:
                print(0)