import sys

input = sys.stdin.readline

bridge = [0] * 101


def move(position, direction):
    if direction == "R":
        for i in range(position + 1, 101):
            bridge[i] += 1
    else:
        for i in range(position - 1, 0, -1):
            bridge[i] += 1


P = int(input())
N = int(input())
for _ in range(N):
    position, direction = input().split()
    move(int(position), direction)

blue, red, green = 0, 0, 0
for i in range(1, 101):
    num = bridge[i]
    if num % 3 == 0:
        blue += 1
    elif num % 3 == 1:
        red += 1
    else:
        green += 1

print(f"{P * (blue / 100):.2f}")
print(f"{P * (red / 100):.2f}")
print(f"{P * (green / 100):.2f}")
