import sys

input = sys.stdin.readline


def find_k(N, from_to):
    visited = [False] * (N + 1)

    current = 1
    count = 0

    while not visited[current]:
        visited[current] = True
        current = from_to[current]
        count += 1

        if current == N:
            return count

    return 0


T = int(input())
for _ in range(T):
    N = int(input())
    from_to = [0] * (N + 1)

    for i in range(1, N + 1):
        from_to[i] = int(input())

    print(find_k(N, from_to))
