import sys
input = sys.stdin.readline

N = int(input())

before = input().strip()
after = input().strip()

is_duramuri = True

def first_condition(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False
    
def second_condition(w1, w2):
    if w1[0] == w2[0] and w1[-1] == w2[-1]:
        return True
    else:
        return False
    
def third_condition(w1, w2):
    vowels = "aeiou"
    w1_no_vowels = [char for char in w1 if char not in vowels]
    w2_no_vowels = [char for char in w2 if char not in vowels]
    
    if w1_no_vowels == w2_no_vowels:
        return True
    else:
        return False

if first_condition(before, after) and second_condition(before, after) and third_condition(before, after):
    print("YES")
else:
    print("NO")