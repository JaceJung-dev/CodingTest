import sys

input = sys.stdin.readline

while True:
    try:
        s, t = input().split()

        i = 0

        for char in t:
            if i < len(s) and s[i] == char:
                i += 1

        if i == len(s):
            print("Yes")
        else:
            print("No")
    except:
        break
