import sys
input = sys.stdin.readline

pin = input().strip()
pattern = input().strip()
index = 0
new_pin = ""

for char in pattern:
    if char.isupper():
        temp = ord(char) - ord("A") + 1
        index += temp
    else:
        temp = ord(char) - ord("a") + 1
        new_pin += pin[index:index + temp]
        index += temp      

answer = 0
if len(pin) == index:
    for n in new_pin:
        answer += int(n)
    print(answer)
else:
    print("non sequitur")
        
        
        