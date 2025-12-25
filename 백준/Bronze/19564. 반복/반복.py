import sys

input = sys.stdin.readline

word = input().strip()

count = 1
for i in range(1, len(word)):
    prev, curr = word[i - 1], word[i]

    if ord(prev) >= ord(curr):
        count += 1

print(count)
