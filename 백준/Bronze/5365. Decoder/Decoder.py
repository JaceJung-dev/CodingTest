import sys
input = sys.stdin.readline

n = int(input())
coded_msg = input().rstrip().split()

prev_word = " "
decoded_msg = ""
for word in coded_msg:
    idx = len(prev_word) - 1
    try:
        decoded_msg += word[idx]
    except IndexError:
        decoded_msg += " "
        
    prev_word = word
    
print(decoded_msg)
    