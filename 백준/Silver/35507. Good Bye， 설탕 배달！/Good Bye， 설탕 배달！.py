import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    max_a = 0
    max_b = 0
    max_c = 0

    is_ok = True

    for i in range(1, N + 1):
        a, b, c, p = map(int, input().split())

        max_a = max(max_a, a)
        max_b = max(max_b, b)
        max_c = max(max_c, c)

        if max_a + max_b + max_c + i > p:
            is_ok = False

    print("YES" if is_ok else "NO")
