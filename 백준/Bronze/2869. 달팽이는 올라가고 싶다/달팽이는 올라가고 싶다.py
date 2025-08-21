import sys
import math
input = sys.stdin.readline

A, B, V = map(int, input().split())
gap = A - B

days = 1 + math.ceil((V - A) / gap)
    
print(days)
