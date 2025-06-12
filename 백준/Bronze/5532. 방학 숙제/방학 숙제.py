import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

lang_hw = math.ceil(A / C)
math_hw = math.ceil(B / D)

if lang_hw > math_hw:
    print(L - lang_hw)
else:
    print(L - math_hw)