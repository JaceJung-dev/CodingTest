import sys

input = sys.stdin.readline

word = input().strip()
sub = input().strip()

if sub in word:
    print(1)
else:
    print(0)
