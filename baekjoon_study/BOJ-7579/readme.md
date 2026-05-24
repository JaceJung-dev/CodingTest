# BOJ 7579 - 앱

## 문제

- 링크: https://www.acmicpc.net/problem/7579
- 태그: 다이나믹 프로그래밍, 배낭 문제

## 접근 방식

"M 바이트 이상 확보"가 목표이고, 메모리는 최대 10⁷까지 가지만 **비용(c)의 총합은 최대 100×100 = 10,000**으로 작다는 점이 핵심. 따라서 **비용을 DP의 차원으로** 잡는 변형 배낭이 정답.

- `dp[n][c]` = 1..n번 앱 중에서 **비용 합이 정확히 c 이하**가 되도록 비활성화했을 때 **확보 가능한 메모리의 최댓값**
- 점화식 (앱 n을 비활성화 할지 말지):

```
dp[n][c] = max(
    dp[n-1][c],                          # 앱 n을 두기
    dp[n-1][c - costs[n]] + mems[n]      # 앱 n을 비활성화 (cost[n]만큼 비용 사용)
)
```

- 답: `dp[N][c] >= M`을 만족하는 최소 c

메모리 차원이 아니라 비용 차원으로 DP를 잡는다는 발상이 이 문제의 포인트. (1 ≤ N ≤ 100, 0 ≤ c ≤ 100 → 비용 합 ≤ 10,000)

## 풀이

### Solution 1 — Bottom-Up

```python
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

MAX = 10001
INF = 10**12

N, M = map(int, input().split())
mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

dp = [[0] * MAX for _ in range(N + 1)]

for n in range(1, N + 1):
    for c in range(0, MAX):
        dp[n][c] = dp[n - 1][c]
        if c - costs[n] >= 0:
            dp[n][c] = max(dp[n][c], dp[n - 1][c - costs[n]] + mems[n])

ans = INF
for c in range(0, MAX):
    if dp[N][c] >= M:
        ans = min(ans, c)

print(ans)
```

- `MAX = 10001`은 비용 합의 상한 (100 앱 × 100 비용 + 1)
- 표준 0/1 배낭 형태: 각 앱마다 "버린다 / 비활성화한다" 두 선택
- 마지막에 c를 0부터 훑으며 처음으로 메모리 ≥ M인 c가 답

### Solution 2 — Top-Down (메모이제이션)

```python
MAX = 10001
INF = 10**12


def func(n, c):

    if n == 0:
        return 0
    if dp[n][c] != -1:
        return dp[n][c]

    dp[n][c] = func(n - 1, c)
    if c - costs[n] >= 0:
        dp[n][c] = max(dp[n][c], func(n - 1, c - costs[n]) + mems[n])

    return dp[n][c]


N, M = map(int, input().split())
mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

dp = [[-1] * MAX for _ in range(N + 1)]

# 파라매트릭 서치도 가능
ans = INF
for c in range(0, MAX):
    if func(N, c) >= M:
        ans = min(ans, c)

print(ans)
```

- 같은 점화식을 메모이제이션으로 풀어 동일 결과
- "파라매트릭 서치도 가능" 메모: `dp[N][c] >= M`이 c에 대해 단조이므로 이분 탐색으로 최소 c 탐색 가능 (단, dp 자체는 모든 c에 대해 채워야 해서 본질적 이득은 작음)

## 복잡도

|            | 시간                    | 공간     |
| ---------- | ----------------------- | -------- |
| Solution 1 | O(N × C) = O(100 × 10⁴) | O(N × C) |
| Solution 2 | O(N × C)                | O(N × C) |

여기서 C는 비용 합 상한. 1차원으로 압축하면 공간 O(C)도 가능 (앱 n에 대해 c를 큰 쪽부터 훑어 갱신).

## 배운 점

- "용량/무게가 큰데 가치(여기선 비용)가 작다"면 **DP 차원을 가치 쪽으로** 잡는 것이 핵심 트릭 (반대 방향 0/1 배낭)
- 12865 평범한 배낭과 정확히 같은 점화식이지만 **DP 인덱스의 의미**가 반대 (12865는 무게가 작아 무게로 인덱싱, 7579는 비용이 작아 비용으로 인덱싱)
- "최소 비용으로 X 이상 확보" 류 문제는 보통 **dp[자원] = 그 자원을 쓰면 얻을 수 있는 최대 효용** 으로 정의한 뒤 마지막에 조건을 만족하는 최소 자원을 찾는 패턴
- `dp[N][c]`는 c에 대해 단조 비감소 → 이분 탐색(파라매트릭)도 적용 가능
