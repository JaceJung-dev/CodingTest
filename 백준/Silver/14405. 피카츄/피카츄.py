import sys
input = sys.stdin.readline

word = input().rstrip()
i = 0

while i < len(word):
    if word.startswith("pi", i):
        i += 2
    elif word.startswith("ka", i):
        i += 2
    elif word.startswith("chu", i):
        i += 3
    else:
        print("NO")
        break
else:
    print("YES")
        