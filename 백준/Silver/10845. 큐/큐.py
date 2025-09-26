import sys


input = sys.stdin.readline


class Queue:

    def __init__(self):
        self.queue = []

    def push(self, num):
        self.queue.append(num)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.queue:
            return 0
        else:
            return 1

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return -1


queue = Queue()

N = int(input())

for _ in range(N):
    cmd = input().split()

    method = getattr(queue, cmd[0])

    if cmd[0] == "push":
        method(cmd[1])
    else:
        action = method()
        print(action)
