import sys

input = sys.stdin.readline

target = [
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"],
    ["M", "N", "O", "."],
]

pos_map = {}

for i in range(4):
    for j in range(4):
        if target[i][j] != ".":
            pos_map[target[i][j]] = (i, j)

total_move = 0

for i in range(4):
    row = input().strip()
    for j in range(4):
        char = row[j]
        if char == ".":
            continue

        oi, oj = pos_map[char]
        total_move += abs(oi - i) + abs(oj - j)

print(total_move)
