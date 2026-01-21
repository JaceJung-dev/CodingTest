import sys

input = sys.stdin.readline

base = ["10001", "10001", "11111", "10001", "11111"]

N = int(input())
treated = []
for row in base:
    for _ in range(N):
        new_row = row.replace("1", "@" * N).replace("0", " " * N)
        print(new_row)
