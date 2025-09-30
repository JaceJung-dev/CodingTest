import sys

input = sys.stdin.readline

N = int(input())
targets = [int(input()) for _ in range(N)]

stack = []
answer = []
num = 1

for target in targets:

    while num <= target:
        stack.append(num)
        answer.append("+")
        num += 1

    if stack[-1] == target:
        stack.pop()
        answer.append("-")
    else:
        answer = ["NO"]
        break

print("\n".join(answer))