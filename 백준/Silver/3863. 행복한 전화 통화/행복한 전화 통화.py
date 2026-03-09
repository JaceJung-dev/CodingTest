import sys

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    calls = []
    for _ in range(N):
        source, dest, start, duration = map(int, input().split())
        end = start + duration
        calls.append((start, end))

    for _ in range(M):
        start, duration = map(int, input().split())
        end = start + duration

        count = 0
        for call_start, call_end in calls:
            if call_start < end and start < call_end:
                count += 1

        print(count)
