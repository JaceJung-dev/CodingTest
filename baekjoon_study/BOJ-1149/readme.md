# BOJ 1149 - RGB거리

## 문제

- 링크: https://www.acmicpc.net/problem/1149
- 태그: DP

## 접근 방식

N개의 집을 빨강/초록/파랑 중 하나로 칠하되, **인접한 집은 같은 색이 불가**. 모든 집을 칠하는 최소 비용을 구하는 문제.

- `dp[n][c]` = n번째 집을 c색(0/1/2)으로 칠했을 때 1..n번 집을 칠하는 데 든 최소 누적 비용
- n번째 집에 c색을 칠하려면, n-1번째 집은 c가 아닌 **나머지 두 색 중 최솟값**을 선택

점화식:

```
dp[n][0] = min(dp[n-1][1], dp[n-1][2]) + matrix[n][0]
dp[n][1] = min(dp[n-1][0], dp[n-1][2]) + matrix[n][1]
dp[n][2] = min(dp[n-1][0], dp[n-1][1]) + matrix[n][2]
```

`matrix`에 `[0, 0, 0]` 패딩 한 줄을 앞에 두어 1-indexed로 쓰면, `dp[0] = [0, 0, 0]`이 자연스럽게 base case 역할 → 별도 초기화 불필요 (n=1 계산 시 `min(0, 0) + matrix[1][c] = matrix[1][c]` 가 됨).

## 풀이

### Solution — Bottom-Up DP

```python
import sys

input = sys.stdin.readline

# input
N = int(input())
matrix = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

# solve
dp = [[0, 0, 0] for _ in range(N + 1)]

for n in range(1, N + 1):
    dp[n][0] = min(dp[n - 1][1], dp[n - 1][2]) + matrix[n][0]
    dp[n][1] = min(dp[n - 1][0], dp[n - 1][2]) + matrix[n][1]
    dp[n][2] = min(dp[n - 1][0], dp[n - 1][1]) + matrix[n][2]

print(min(dp[N]))
```

- `matrix`와 `dp` 모두 0번 행을 0으로 패딩해 1-indexed
- `dp[0]`이 `[0, 0, 0]`이므로 `n = 1`부터 점화식이 그대로 성립 (`dp[1][c] = matrix[1][c]`)
- 최종 답은 `min(dp[N])` — 마지막 집을 어느 색으로 칠했든 그 중 최솟값

## 복잡도

- 시간: O(N) — 각 집마다 3색 계산 (상수)
- 공간: O(N) — `dp[N+1][3]` (필요시 이전 행만 들고가는 O(1) 최적화 가능)

## 배운 점

- 상태를 색깔 차원으로 분리하여 `dp[n][색]`으로 정의하면 인접 조건을 자연스럽게 처리 가능 → "직전 집의 색이 무엇이었는가"를 상태에 담는 것이 핵심
- 이전 행의 **나머지 두 색에서 `min`** 을 취하는 점화식은 "현재 색을 제외" 조건을 그대로 식으로 옮긴 형태
- 공간 최적화: 이전 행만 필요하므로 두 줄짜리 배열(roll-over)로 O(1) 공간까지 줄일 수 있음
