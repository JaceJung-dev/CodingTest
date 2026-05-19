# BOJ 1912 - 연속합

## 문제

- 링크: https://www.acmicpc.net/problem/1912
- 태그: 다이나믹 프로그래밍

## 접근 방식

연속된 부분 수열의 합 중 최댓값을 구하는 **카데인(Kadane) 알고리즘** 문제. `dp[n]`를 "n번째 원소를 **반드시 포함하는** 연속하는 부분 수열의 최대 합"으로 정의:

```
dp[i] = max(0, dp[n-1]) + nums[n]
      = max(dp[n-1] + nums[n], nums[n])
```

직전 부분합이 음수면 "리셋(혼자 새로 시작)"이 더 유리하다는 관찰. 정답은 `max(dp[1..N])`.

## 풀이

### Solution 1 — Bottom-Up (반복)

```python
import sys

input = sys.stdin.readline

# input
N = int(input())
nums = [0] + list(map(int, input().split()))

# solve
dp = [0] * (N + 1)

for n in range(1, N + 1):
    dp[n] = max(0, dp[n - 1]) + nums[n]

print(max(dp[1:]))
```

- `dp[n] = max(0, dp[n-1]) + nums[n]` → 직전 합이 음수면 0으로 리셋 후 새로 시작
- 정답은 모든 `dp[n]` 중 최댓값

### Solution 2 — Top-Down (메모이제이션)

```python
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

INF = 10**12


def func(n):

    # base case
    if n == 0:
        return 0

    if dp[n] != -INF:
        return dp[n]

    # recursive case
    dp[n] = max(0, func(n - 1)) + nums[n]

    return dp[n]


# input
N = int(input())
nums = [0] + list(map(int, input().split()))

# solve
dp = [-INF] * (N + 1)

ans = -INF
for i in range(1, N + 1):
    ans = max(ans, func(i))

print(ans)
```

- `nums`를 `[0]`으로 패딩해 1-indexed 사용
- `func(n)` = "n번째 원소를 포함하는 최대 부분합", `func(0) = 0` (시작 직전 가상의 빈 수열)
- 메모 미스(`-INF`)일 때만 재귀 호출 → 동일 인덱스는 한 번만 계산

## 복잡도

|           | 시간 | 공간 |
| --------- | ---- | ---- |
| Bottom-Up | O(N) | O(N) |
| Top-Down  | O(N) | O(N) |

## 배운 점

- "연속 부분합 최댓값" 유형은 **카데인 알고리즘** 한 줄 점화식으로 해결: `dp[n] = max(dp[n-1] + nums[n], nums[n])`
- `dp[n]`를 "n를 포함하는" 으로 정의하면 점화식이 단순해지고, 정답은 마지막에 `max(dp)`로 추출
- 모든 원소가 음수인 경우, 답은 음수 중 최댓값이 됨 → "0으로 리셋"이 답이 되지 않도록 **dp 정의에서 빈 부분합을 허용하지 않는 것**이 핵심
