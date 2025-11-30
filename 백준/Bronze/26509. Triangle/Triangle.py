import sys

input = sys.stdin.readline


def is_right_triangle(arr):
    a, b, c = sorted(arr)
    if c * c == a * a + b * b:
        return True
    return False


N = int(input())

for _ in range(N):
    first = sorted(list(map(int, input().split())))
    second = sorted(list(map(int, input().split())))

    if is_right_triangle(first) and is_right_triangle(second) and first == second:
        print("YES")
    else:
        print("NO")
