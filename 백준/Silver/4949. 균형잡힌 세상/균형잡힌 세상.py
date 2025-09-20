import sys

input = sys.stdin.readline


def is_balanced(sentence):
    stack = []

    for char in sentence:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if stack and (
                (stack[-1] == "(" and char == ")") or (stack[-1] == "[" and char == "]")
            ):
                stack.pop()
            else:
                return False
    return not stack


while True:
    sentence = input().rstrip()

    if sentence == ".":
        break

    if is_balanced(sentence):
        print("yes")
    else:
        print("no")
