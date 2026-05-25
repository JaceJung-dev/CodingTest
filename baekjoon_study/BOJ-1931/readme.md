# BOJ 1931 - 회의실 배정

## 문제

- 링크: https://www.acmicpc.net/problem/1931
- 태그: 그리디 알고리즘, 정렬

## 접근 방식

겹치지 않게 회의를 가능한 한 많이 배치하는 **활동 선택(Activity Selection)** 문제. 정석은 **끝나는 시간 기준 오름차순 정렬 후 그리디**:

- 직관: "가장 빨리 끝나는 회의를 먼저 잡으면, 뒷쪽에 남는 시간이 가장 많다" → 이후 선택 가능한 후보가 가장 많아짐
- 시작 시간이 같을 때를 위해 보조 키로 시작 시간도 같이 정렬 (끝=시작인 회의 처리)
- 한 회의가 끝나는 것과 동시에 다음 회의가 시작 가능 (`<=` 비교)

DP로도 풀 수 있는데, 시간 좌표 범위가 매우 커서 (최대 2³¹−1) **좌표 압축**이 필요함.

## 풀이

### Solution 1 — Greedy (끝나는 시간 정렬)

```python
import sys

input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
cur_e = 0
for s, e in meetings:
    if cur_e <= s:
        count += 1
        cur_e = e

print(count)
```

- `(끝, 시작)` 순으로 정렬 → 동률은 시작 시간이 작은 쪽이 먼저
- `cur_e`는 마지막에 잡은 회의의 종료 시각, 다음 회의의 시작 시각이 그보다 크거나 같으면 잡음
- O(N log N) — N ≤ 10⁵라 충분

### Solution 2 — DP + 좌표 압축

```python
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
```

- 등장하는 시각만 모아 **좌표 압축** → DP 인덱스 크기를 `T = O(N)`으로 축소
- `dp[t]` = 압축된 시각 t까지 끝나는 것을 마지막으로 했을 때의 최대 선택 회의 수
- 점화식: `dp[t] = max(dp[t-1], max(dp[s] + 1 for (s, t) in 회의))`
  - 시각 t를 끝으로 하는 회의 `(s, t)`마다 `dp[s] + 1`을 후보로
  - 그 외엔 `dp[t-1]` 그대로 전달
- 복잡도: O(N log N) (정렬 + 압축) + O(T + 회의 수) = O(N log N)

## 복잡도

|            | 시간       | 공간 |
| ---------- | ---------- | ---- |
| Solution 1 | O(N log N) | O(N) |
| Solution 2 | O(N log N) | O(N) |

## 배운 점

- 활동 선택 그리디의 정석은 **끝나는 시간 오름차순**이지 시작 시간 기준이 아님 (시작 시간 기준은 반례 있음)
- 동률 처리: `(end, start)` 보조키로 정렬하면 "0 0", "1 1" 같이 시작=끝인 회의도 정상 처리 (이 정렬을 안 하면 같은 끝 시각 내에서 시작이 늦은 게 먼저 와 다음 후보를 잘못 막을 수 있음)
- 시간 좌표가 매우 클 때(2³¹) DP를 쓰려면 **좌표 압축**이 필수 → "등장 값만 모아 정렬 후 인덱스로 치환"
