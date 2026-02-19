import sys

input = sys.stdin.readline

direction, N = input().split()
N = int(N)

arr = [input().split() for _ in range(N)]

flip = {
    "1": "1",
    "2": "5",
    "5": "2",
    "8": "8",
}

if direction == "L" or direction == "R":
    arr = [row[::-1] for row in arr]
else:
    arr = arr[::-1]

for j in range(N):
    for i in range(N):
        arr[j][i] = flip.get(arr[j][i], "?")

for row in arr:
    print(*row)
