import sys
input = sys.stdin.readline

n = int(input())
anagram = set()

for _ in range(n):
    word = input().rstrip()
    sorted_word = "".join(sorted(word))
    
    if sorted_word not in anagram:
        print(word)
        anagram.add(sorted_word)