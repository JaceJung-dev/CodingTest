import sys


def is_VPS(string):
    stack = []

    for s in string:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack and (stack[-1] == "("):
                stack.pop()
            else:
                return False

    return not stack

if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        s = input().strip()

        if is_VPS(s):
            print("YES")
        else:
            print("NO")
