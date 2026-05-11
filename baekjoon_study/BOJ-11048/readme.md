# BOJ 11048 - 이동하기

## 문제

- 링크: https://www.acmicpc.net/problem/11048
- 태그: DP

## 접근 방식

(1,1)에서 (N,M)까지 오른쪽, 아래, 대각선으로만 이동하며 사탕을 최대로 모으는 문제. 두 가지 방식으로 구현:

1. **Bottom-up DP** - 반복문으로 작은 칸부터 채워나감
2. **Top-down DP (메모이제이션)** - 재귀 + dp 배열 캐싱

## 풀이

### Solution 1 — Bottom-up DP

```python
# input
N, M = map(int, input().split())
matrix = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# solve
dp = [[0] * (M + 1) for _ in range((N + 1))]

for n in range(1, N + 1):
    for m in range(1, M + 1):
        dp[n][m] = max(dp[n - 1][m], dp[n - 1][m - 1], dp[n][m - 1]) + matrix[n][m]

print(dp[N][M])
```

- 0번 행/열을 패딩으로 추가하여 경계 처리 간소화
- `dp[i][j]` = 위, 왼쪽 위 대각선, 왼쪽에서 오는 값 중 최대 + 현재 칸 사탕

### Solution 2 — Top-down DP (메모이제이션)

```python
def func(i, j):
    global dp

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = max(func(i - 1, j), func(i - 1, j - 1), func(i, j - 1)) + matrix[i][j]

    return dp[i][j]
```

- `dp[i][j] != -1`이면 캐시 반환
- 0번 행/열을 base case(0)로 초기화

### 공통

- 점화식: `dp[n][m] = max(dp[n - 1][m], dp[n - 1][m - 1], dp[n][m - 1]) + matrix[n][m]`

## 복잡도

- 시간: O(N × M) — 각 칸을 한 번씩 계산
- 공간: O(N × M) — dp 배열 + matrix 배열

## 배운 점

- 0번 행/열 패딩을 넣으면 `n-1`, `m-1` 경계 체크 없이 점화식을 깔끔하게 작성 가능
- Bottom-up과 Top-down이 동일한 점화식을 사용하지만, Bottom-up은 반복문, Top-down은 재귀+캐싱으로 구현 방식이 다름
- 대각선 이동은 사실상 `max(위, 왼쪽)`에 항상 포함되므로 생략해도 결과가 같음
