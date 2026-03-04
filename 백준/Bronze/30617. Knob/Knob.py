import sys

input = sys.stdin.readline

T = int(input())
prev_l, prev_r = 0, 0
score = 0
for _ in range(T):
    curr_l, curr_r = map(int, input().split())
    if curr_l == curr_r != 0:
        score += 1

    if curr_l != 0 and curr_l == prev_l:
        score += 1

    if curr_r != 0 and curr_r == prev_r:
        score += 1

    prev_l, prev_r = curr_l, curr_r

print(score)
