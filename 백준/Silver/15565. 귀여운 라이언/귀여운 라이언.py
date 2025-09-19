import sys

input = sys.stdin.readline


def get_min_length(N, K, dolls):
    ryan_pos = [i for i in range(N) if dolls[i] == 1]
    l = len(ryan_pos)
    min_length = float("inf")

    if l < K:
        return -1
    else:
        for i in range(0, l - K + 1):
            length = ryan_pos[i + K - 1] - ryan_pos[i] + 1
            min_length = min(min_length, length)
        return min_length


if __name__ == "__main__":
    N, K = map(int, input().split())
    dolls = list(map(int, input().split()))

    min_length = get_min_length(N, K, dolls)

    print(min_length)
