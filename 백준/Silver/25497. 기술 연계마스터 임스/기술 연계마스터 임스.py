import sys

input = sys.stdin.readline

N = int(input())
commands = input().strip()
l_combo, s_combo = [], []

count = 0
for command in commands:
    if command.isdigit():
        count += 1

    if command == "L":
        l_combo.append(command)

    if command == "S":
        s_combo.append(command)

    if command == "R":
        if l_combo:
            l_combo.pop()
            count += 1
        else:
            break

    if command == "K":
        if s_combo:
            s_combo.pop()
            count += 1
        else:
            break

print(count)
