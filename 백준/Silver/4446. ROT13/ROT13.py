import sys

input = sys.stdin.readline

vowels = "a i y e o u"
vowels = list(vowels.split())
consonants = "b k x z n h d c w g p v j q t s r l m f"
consonants = list(consonants.split())

char_map = {}

for i, vowel in enumerate(vowels):
    char_map[vowel] = vowels[(i + 3) % 6]

for i, consonant in enumerate(consonants):
    char_map[consonant] = consonants[(i + 10) % 20]

char_map.update({k.upper(): v.upper() for k, v in char_map.items()})


for line in sys.stdin:
    sentence = line.rstrip("\n")
    converted = ""
    for char in sentence:
        if char in char_map:
            converted += char_map[char]
        else:
            converted += char

    print(converted)
