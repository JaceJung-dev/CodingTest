import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

std_word = "SciComLove"
word = [std_word[i % 10] for i in range(N)]

count = sum(1 for char in word if char.isupper())

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
