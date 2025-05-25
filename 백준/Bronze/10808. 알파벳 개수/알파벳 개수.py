word = input()

alphabet_list = [0] * 26

for char in word:
    idx = ord(char) - ord("a")
    alphabet_list[idx] += 1

print(*alphabet_list)
    