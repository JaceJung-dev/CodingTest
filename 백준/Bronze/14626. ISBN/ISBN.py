import sys
input = sys.stdin.readline

isbn = input().rstrip()

total = 0
unknown_idx = None
unknown = -1
for i, v in enumerate(isbn[:-1]):
    if v == "*":
        unknown_idx = i
        continue
        
    if i % 2 == 0:
        total += int(v)
    else:
        total += 3 * int(v)
        
m = int(isbn[-1])
r = (10 - (total + m) % 10) % 10

if unknown_idx % 2 == 0:
    unknown = r
else:
    unknown = (r * 7) % 10
    
print(unknown)