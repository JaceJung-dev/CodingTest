import sys
input = sys.stdin.readline

def convert_to_decimal(num: str, base: int) -> int:
    decimal = 0
    num = num[::-1]
    
    for i, digit in enumerate(num):
        if digit.isdigit():
            decimal += int(digit) * (base ** i)
        else:
            decimal += (ord(digit) - ord("A") + 10) * (base ** i)
    return decimal

def decimal_to_another_base(decimal: int, base: int) -> str:
    
    if decimal == 0:
        return 0
    
    another_base = ""
    
    while decimal > 0:
        digit = decimal % base
        
        if digit >= 10:
            another_base += chr(ord("A") - 10 + digit)
        else:
            another_base += str(digit)
            
        decimal //= base
            
    return another_base[::-1]
    
N = int(input())
for _ in range(N):
    x, y, z = input().strip().split(" ")
    x, y = int(x), int(y)
    
    decimal = convert_to_decimal(z, x)
    
    another_base_num = decimal_to_another_base(decimal, y)
    
    print(another_base_num)
