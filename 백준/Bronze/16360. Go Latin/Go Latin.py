import sys
input = sys.stdin.readline

conv_dict = {"a": "as", "i": "ios", "y": "ios", "l": "les", "n": "anes", "ne": "anes",
            "o": "os", "r": "res", "t": "tas", "u": "us", "v": "ves", "w": "was"}

N = int(input())
for _ in range(N):
    word = input().rstrip()
    
    for i, v in conv_dict.items():
        if word.endswith(i):
            if i == "ne":
                word = word[:-2] + v
                break
            else:
                word = word[:-1] + v
                break
    else:
        word = word + "us"
        
    print(word)