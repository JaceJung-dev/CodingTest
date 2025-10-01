import sys

input = sys.stdin.readline


class Set:

    def __init__(self):
        self.set = []

    def add(self, x):
        if x not in self.set:
            self.set.append(x)

    def remove(self, x):
        if x in self.set:
            self.set.remove(x)

    def check(self, x):
        if x in self.set:
            return 1
        else:
            return 0

    def toggle(self, x):
        if x in self.set:
            self.set.remove(x)
        else:
            self.set.append(x)

    def all(self):
        self.set = [n for n in range(1, 21)]

    def empty(self):
        self.set = []


S = Set()

M = int(input())
for _ in range(M):
    commend = input().split()

    method = getattr(S, commend[0])

    if commend[0] == "all" or commend[0] == "empty":
        method()
    elif commend[0] == "check":
        print(method(int(commend[1])))
    else:
        method(int(commend[1]))
