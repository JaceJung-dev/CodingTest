import sys

input = sys.stdin.readline


def get_count(arr, length):
    count = 0
    for line in arr:
        count += line // length

    return count


K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

min_len, max_len = 1, max(cables)
final_length = 0

while min_len <= max_len:
    middle = (min_len + max_len) // 2

    count = get_count(cables, middle)

    if count >= N:
        final_length = middle
        min_len = middle + 1
    else:
        max_len = middle - 1

print(final_length)
