import sys

input = sys.stdin.readline

N = int(input())
moves = {}
for _ in range(N):
    cur, dirs, step = input().split()
    moves[int(cur)] = (dirs, int(step))
cur_pos = int(input())

while moves:
    next_step = moves.pop(cur_pos)
    if next_step[0] == "L":
        cur_pos -= next_step[1]
    else:
        cur_pos += next_step[1]
        
print(cur_pos)
