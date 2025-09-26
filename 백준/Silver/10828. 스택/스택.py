import sys


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return 0
        else:
            return 1

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1

input = sys.stdin.readline

stack = Stack()

N = int(input())
for _ in range(N):
    cmd = input().split()
    func = cmd[0]

    method = getattr(stack, func)

    if func == "push":
        method(int(cmd[1]))
    else:
        res = method()
        print(res)
