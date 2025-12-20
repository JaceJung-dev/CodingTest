import sys

input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    K, audience = input().split()
    K = int(K)
    audience = list(map(int, audience))

    addition = 0
    accumulation = audience[0]
    for j in range(1, K + 1):
        if j > accumulation:
            gap = j - accumulation
            accumulation += audience[j] + gap
            addition += gap
        else:
            accumulation += audience[j]
    print(f"Case #{i}: {addition}")
