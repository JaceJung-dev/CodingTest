import sys

input = sys.stdin.readline

N = int(input())
word = "SciComLove"

if N % 2 == 0:
    print(word)
else:
    print(word[::-1])
