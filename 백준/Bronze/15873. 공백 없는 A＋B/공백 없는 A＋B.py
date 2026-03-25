import sys

input = sys.stdin.readline

N = input().strip()
length = len(N)

if length == 2:
    print(int(N[0]) + int(N[-1]))
elif length == 3:
    if N[:2] == "10":
        print(10 + int(N[-1]))
    else:
        print(int(N[0]) + 10)
else:
    print(20)