import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, valid_num = map(int, input().split())
    count = 0
    bit = 0
    binary_N = ""
    
    while N > 0:
        binary_N += str(N % 2)
        N //= 2
        
    for n in binary_N:
        if n == "1":
            count += 1

            
    if count % 2 == 0:
        bit = 0
    else:
        bit = 1
        
    if bit == valid_num:
        print("Valid")
    else:
        print("Corrupt")
        