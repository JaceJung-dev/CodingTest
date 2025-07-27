import sys
input = sys.stdin.readline

word = input().strip()

while True:
    if word.startswith("pi") or word.startswith("ka"):
        word = word[2:]
    elif word.startswith("chu"):
        word = word[3:]
    else:
        break
        
if word:
    print("NO")
else:
    print("YES")
