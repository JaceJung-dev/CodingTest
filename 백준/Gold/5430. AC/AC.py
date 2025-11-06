import sys
from collections import deque

input = sys.stdin.readline


def do_func(functions, N, arr_str):
    if N == 0:
        queue = deque()
    else:
        queue = deque(arr_str[1:-1].split(","))

    reverse_flag = False

    for f in functions:
        if f == "R":
            reverse_flag = not reverse_flag
        elif f == "D":
            if not queue:
                return "error"

            if reverse_flag:
                queue.pop()
            else:
                queue.popleft()

    if reverse_flag:
        queue.reverse()

    return f"[{','.join(map(str, queue))}]"


T = int(input())
for _ in range(T):
    functions = input().strip()
    N = int(input())
    arr_str = input().strip()

    print(do_func(functions, N, arr_str))
