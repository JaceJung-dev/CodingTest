import sys

input = sys.stdin.readline

N, M = map(int, input().split())

class_end_time = [0] * (N + 1)
for _ in range(M):
    k, s, e = map(int, input().split())

    if s >= class_end_time[k]:
        class_end_time[k] = e
        print("YES")
    else:
        print("NO")
