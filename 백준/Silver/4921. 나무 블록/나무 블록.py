import sys

input = sys.stdin.readline


# 0: 편평,
# 1: 볼록네모, 2: 볼록반원,
# 3: 오목네모, 4: 오목반원,

block_shape = {
    "1": (0, 3),
    "2": (3, 0),
    "3": (3, 3),
    "4": (1, 1),
    "5": (1, 4),
    "6": (4, 1),
    "7": (4, 4),
    "8": (2, 2),
}


def is_connect(prev_right, curr_left):
    if (prev_right == 1 and curr_left == 3) or (prev_right == 3 and curr_left == 1):
        return True
    if (prev_right == 2 and curr_left == 4) or (prev_right == 4 and curr_left == 2):
        return True
    return False


def is_valid(seq):
    n = len(seq)

    if seq[0] != "1" or seq[-1] != "2":
        return False

    for i in range(n - 1):
        prev_right = block_shape[seq[i]][1]
        curr_left = block_shape[seq[i + 1]][0]

        if not is_connect(prev_right, curr_left):
            return False

    return True


i = 1
while True:
    seq = input().strip()

    if seq == "0":
        break

    if is_valid(seq):
        print(f"{i}. VALID")
    else:
        print(f"{i}. NOT")

    i += 1
