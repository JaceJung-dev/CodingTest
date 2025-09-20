import sys

input = sys.stdin.readline

while True:
    sentence = input().rstrip()

    if sentence == ".":
        break

    stack = []

    for char in sentence:

        if stack:
            cur = stack.pop()

            if cur == "(" and char == ")":
                continue
            elif cur == "[" and char == "]":
                continue
            else:
                stack.append(cur)

        if char in ["(", ")", "[", "]"]:
            stack.append(char)

    if stack:
        print("no")
    else:
        print("yes")
