vowels = ["a", "e", "i", "o", "u"]

while True:
    count = 0
    sentence = input().lower()
    
    if sentence == "#":
        break
    
    for alphabet in sentence:
        if alphabet in vowels:
            count += 1
    print(count)
    