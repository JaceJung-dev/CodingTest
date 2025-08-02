import sys

N, B = map(int, sys.stdin.readline().split(" "))
conversed_num = ""

while N > 0:
    num = N % B
    if num >= 10:
        num = chr(ord("A") - 10 + num)
        conversed_num += num
    else:
        conversed_num += str(num)
    N = N // B
    
print(conversed_num[::-1])