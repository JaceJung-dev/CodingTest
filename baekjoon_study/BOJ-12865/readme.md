# BOJ 12865 - 평범한 배낭

## 문제

- 링크: https://www.acmicpc.net/problem/12865
- 태그: DP, 0/1 Knapsack

## 접근 방식

N개의 물건(무게 W, 가치 V)을 배낭 용량 K 이하로 담을 때 최대 가치를 구하는 **0/1 배낭 문제**. 각 물건을 담거나 담지 않는 두 가지 선택을 재귀/반복으로 탐색.

- `dp[n][k]` = n번째 물건까지 고려했을 때, 용량 k로 얻을 수 있는 최대 가치
- 점화식:
  - `k >= W[n]`이면 `dp[n][k] = max(dp[n-1][k], dp[n-1][k-W[n]] + V[n])`
  - 아니면 `dp[n][k] = dp[n-1][k]`

두 가지 방식으로 구현:

1. **Top-down DP (메모이제이션)** - 재귀 + dp 배열 캐싱
2. **Bottom-up DP** - 반복문으로 작은 상태부터 채워나감

## 풀이

### Solution 1 — Top-down DP

```python
def func(n, k):
    global W, V, dp

    if n == 0 or k == 0:
        return 0

    if dp[n][k] != -1:
        return dp[n][k]

    if k >= W[n]:
        dp[n][k] = max(func(n - 1, k), func(n - 1, k - W[n]) + V[n])
    else:
        dp[n][k] = func(n - 1, k)

    return dp[n][k]
```

- base case: `n == 0` 또는 `k == 0`이면 0 반환
- 담을 수 있으면 `max(담지 않음, 담음)`, 없으면 `담지 않음`만 계산

### Solution 2 — Bottom-up DP

```python
dp = [[0] * (K + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for k in range(1, K + 1):
        dp[n][k] = dp[n - 1][k]

        if k - W[n] >= 0:
            dp[n][k] = max(dp[n][k], dp[n - 1][k - W[n]] + V[n])

print(dp[N][K])
```

- 기본값으로 `dp[n-1][k]`(담지 않음)을 할당하고, 담을 수 있으면 갱신
- 0번 행/열이 자동으로 base case(0)가 됨

## 복잡도

- 시간: O(N × K) — 각 (물건, 용량) 상태를 한 번씩 계산
- 공간: O(N × K) — dp 2차원 배열

## 배운 점

- 0/1 배낭의 기본 점화식: "담지 않음 vs 담음" 중 최댓값
- Top-down은 실제 방문하는 상태만 계산하지만, 재귀 오버헤드와 함수 호출 비용이 있음
- Bottom-up은 모든 상태를 채우지만 반복문이라 더 빠르고 공간 최적화(1D 배열 역순 순회)도 가능
- Top-down에서는 모든 분기에서 `dp[n][k]`에 값을 할당해야 캐시가 올바르게 동작 (else 처리 필수)
