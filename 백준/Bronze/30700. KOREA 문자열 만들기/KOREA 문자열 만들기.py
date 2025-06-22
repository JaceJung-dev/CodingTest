check_list = ["K", "O", "R", "E", "A"]
final_word = ""

word = input()
i = 0
for letter in word:
    if letter == check_list[i % 5]:
        final_word += letter
        i = (i + 1) % 5
        
print(len(final_word))