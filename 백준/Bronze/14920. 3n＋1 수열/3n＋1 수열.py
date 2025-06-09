a = int(input())

n = 1

while True:
    if a == 1:
        print(n)
        break
    
    n += 1
    
    if a % 2 == 0:
        a /=2
    else:
        a = 3 * a + 1