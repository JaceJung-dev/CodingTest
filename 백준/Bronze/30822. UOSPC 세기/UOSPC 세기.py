n = int(input())
word = input()

letter_count = {
    "u": 0,
    "o": 0,
    "s": 0,
    "p": 0,
    "c": 0,
}

for letter in word:
    for k, v in letter_count.items():
        if k == letter:
            letter_count[letter] += 1

min_count = float("inf")
for k, v in letter_count.items():
    if v < min_count:
        min_count = v
        
print(min_count)
   