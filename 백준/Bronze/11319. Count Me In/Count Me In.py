import sys
input = sys.stdin.readline

vowels = ["a", "e", "i", "o", "u"]

S = int(input())
for _ in range(S):
    count_constants = 0
    count_vowels = 0
    sentence = input().lower()
    sentence_str = "".join(sentence.split())
    
    for char in sentence_str:
        if char in vowels:
            count_vowels += 1
        else:
            count_constants += 1
            
    print(count_constants, count_vowels)