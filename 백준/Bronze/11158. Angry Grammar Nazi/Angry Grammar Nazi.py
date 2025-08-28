import sys
input = sys.stdin.readline


N = int(input())
for _ in range(N):
    time = 0
    sentence = input().split()
    
    for i in range(len(sentence)):
        word = sentence[i]
        
        if word == "u" or word == "ur":
            time += 10

        if "lol" in word:
            time += 10
            
        if i < len(sentence) - 1:
            if (word == "should" or word == "would") and sentence[i+1] == "of":
                time += 10
                
    print(time)