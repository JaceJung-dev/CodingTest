import sys

input = sys.stdin.readline

N = int(input())
text_separator = set(input().split())
M = int(input())
num_separator = set(input().split())
K = int(input())
aggregators = set(input().split())
S = int(input())
string = input().strip()

separators = (text_separator | num_separator) - aggregators

current = []
result = []
for char in string:
    if char == " " or char in separators:
        if current:
            result.append("".join(current))
            current = []
    else:
        current.append(char)

if current:
    result.append("".join(current))

for r in result:
    print(r)
