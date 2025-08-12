N = int(input())
r = 0
fin = 1

while fin < N:
    r += 1
    fin += 6 * r
    
print(r + 1)