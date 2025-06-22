pattern = "KOREA"
i = 0
length = 0

word = input()
for letter in word:
    if letter == pattern[i]:
        length += 1
        i = (i + 1) % 5
        
print(length)