import sys
input = sys.stdin.readline

vowels = ["a", "e", "i", "o", "u"]

S = int(input())
for _ in range(S):
    count_constants = 0
    count_vowels = 0
    sentence = input().lower().replace(" ","").strip()

    for char in sentence:
        if char in vowels:
            count_vowels += 1
        else:
            count_constants += 1
            
    print(count_constants, count_vowels)