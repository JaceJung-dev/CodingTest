import sys
input = sys.stdin.readline

while True:
    is_palindrome = False
    word = input().strip()
    
    if word == "#":
        break

    for i in range(len(word)):
        new_word = word[:i] + word[i + 1:]
        
        if new_word == new_word[::-1]:
            is_palindrome = True
            break
            
    if is_palindrome:
        print(new_word)
    else:
        print("not possible")