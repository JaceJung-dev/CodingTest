import sys

input = sys.stdin.readline

whole_s = ""
while True:
    S = input()
    if not S:
        break
    whole_s += S.strip()

total = sum(map(int, whole_s.split(",")))
print(total)
