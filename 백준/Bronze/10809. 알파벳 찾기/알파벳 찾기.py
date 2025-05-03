S = input()
alphabet_index_list = ["-1"] * 26

for i in range(len(S)):
    char = S[i]
    idx = ord(char) - ord("a")
    if alphabet_index_list[idx] == "-1":
        alphabet_index_list[idx] = str(i)
    else:
        continue

print(" ".join(alphabet_index_list))