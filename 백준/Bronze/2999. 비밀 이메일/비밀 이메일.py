import sys

input = sys.stdin.readline


def get_row_col(length):
    row, col = 0, 0
    for r in range(1, int(length**0.5 + 1)):
        if length % r == 0:
            row = r
            col = length // r
    return row, col


msg = input().strip()
N = len(msg)

matrix_row, matrix_col = get_row_col(N)
matrix = [[""] * matrix_col for _ in range(matrix_row)]

for i in range(N):
    r = i % matrix_row
    c = i // matrix_row
    matrix[r][c] = msg[i]

for line in matrix:
    print("".join(line), end="")
print()
