L = int(input())
word = input()
total = 0

for i in range(L):
    char = word[i]
    char_value = ord(char) - ord("a") + 1
    hash_value = char_value * (31 ** (i))
    total += hash_value

print(total % 1234567891)
    