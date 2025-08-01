b, w = map(int, input().split())


def get_side(tile):
    s = 0
    while s ** 2 <= tile:
        s += 1
    
    if s == 1:
        return "Impossible"
    else:
        return s - 1
    
    
if b == w:
    s = get_side(2 * b)
else:
    s = get_side(min(b, w) * 2 + 1)
    
print(s)