N, Q = map(int, input().split())

std_word = "SciComLove"
word = ""
count = 0
word = [std_word[i % 10] for i in range(N)]

for char in word:
    if char.isupper():
        count += 1


for _ in range(Q):
    i = int(input())
    idx = i - 1
    if word[idx].isupper():
        word[idx] = word[idx].lower()
        count -= 1
    else:
        word[idx] = word[idx].upper()
        count += 1
    
    print(count)
