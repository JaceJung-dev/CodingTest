import sys
from itertools import combinations

input = sys.stdin.readline


# solution 1
def is_possible():
    global L, C, letters, selections

    v_cnt = 0

    for char in selections:
        v_cnt += char in vowels
    c_cnt = L - v_cnt

    return v_cnt >= 1 and c_cnt >= 2


def combination(index, level):
    if level == L:
        if is_possible():
            print("".join(selections))
        return

    for i in range(index, C):
        selections.append(letters[i])
        combination(i + 1, level + 1)
        selections.pop()


L, C = map(int, input().split())
letters = input().split()
letters.sort()
vowels = "aeiou"

selections = []
combination(0, 0)


# solution2
def is_possible(arr):
    v_cnt = 0
    for char in arr:
        v_cnt += char in vowels
    c_cnt = L - v_cnt

    return v_cnt >= 1 and c_cnt >= 2


L, C = map(int, input().split())
letters = input().split()
letters.sort()
vowels = "aeiou"


for comb in combinations(letters, L):
    if is_possible(comb):
        print("".join(comb))
