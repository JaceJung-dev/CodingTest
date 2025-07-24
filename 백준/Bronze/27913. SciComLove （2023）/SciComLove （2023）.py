N, Q = map(int, input().split())

std_word = "SciComLove"
word = ""
count = 0
word = [std_word[i % 10] for i in range(N)]

for char in word:
    if char.isupper():
        count += 1


for j in range(Q):
    if word[j].isupper():
        word[j] = word[j].lower()
        count -= 1
    else:
        word[j] = word[j].upper()
        count += 1
    
    print(count)
