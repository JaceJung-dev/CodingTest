import sys
input = sys.stdin.readline

def rotation_value(word):
    return sum(ord(char) - ord("A") for char in word)

def rotate(word, k):
    return "".join(chr((ord(char) - ord("A") + k) % 26 + ord("A")) for char in word) 

def merge(a, b):
    return ''.join(
        chr(((ord(x) - ord("A")) + (ord(y) - ord("A"))) % 26 + ord("A")) for x, y in zip(a, b)
    )
    
    
N = input().strip()
half = len(N) // 2
front, back = N[:half], N[half:]

front_rot = rotate(front, rotation_value(front))
back_rot = rotate(back, rotation_value(back))

print(merge(front_rot, back_rot))
