import sys


input = sys.stdin.readline

N, K = map(int, input().split())

nums = [i for i in range(1, N + 1)]

josephus = []
i = 0
while len(josephus) < N:
    i = (i + K - 1) % len(nums)
    n = nums.pop(i)
    josephus.append(str(n))


print(f"<{', '.join(josephus)}>")