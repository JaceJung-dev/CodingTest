import sys

input = sys.stdin.readline

# Solution 1

# input
N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# solve
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
cur_e = 0
for s, e in meetings:
    if cur_e <= s:
        count += 1
        cur_e = e

print(count)

# Solution 2

# input
N = int(input())

nums = []
times = []

for _ in range(N):
    s, e = map(int, input().split())
    times.append((s, e))
    nums.append(s)
    nums.append(e)

# coordinate compression
nums = sorted(list(set(nums)))
T = len(nums)

convert = dict()
for i, num in enumerate(nums, 1):
    convert[num] = i

# solve
starts = dict()
for i in range(N):
    tmp0, tmp1 = convert[times[i][0]], convert[times[i][1]]
    if tmp1 in starts:
        starts[tmp1].append(tmp0)
    else:
        starts[tmp1] = [tmp0]

for key in starts:
    starts[key].sort()

dp = [0] * (T + 1)
for t in range(1, T + 1):
    dp[t] = dp[t - 1]
    if t in starts:
        for s in starts[t]:
            dp[t] = max(dp[t], dp[s] + 1)

print(dp[T])
