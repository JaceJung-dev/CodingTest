N = int(input())

def get_pinary_num(N):
    a, b = 1, 1
    
    if N == 1 or N == 2:
        return 1
    
    for _ in range(2, N):
        a, b = b, a + b
        
    return b

print(get_pinary_num(N))

    
