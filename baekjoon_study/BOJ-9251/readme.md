# BOJ 9251 - LCS

## 문제

- 링크: https://www.acmicpc.net/problem/9251
- 태그: DP, LCS, 문자열

## 접근 방식

두 문자열의 **최장 공통 부분 수열(Longest Common Subsequence)** 길이를 구하는 대표 DP 문제.

- `dp[n][m]` = `S1[:n]`과 `S2[:m]`의 LCS 길이
- 점화식:
  - `S1[n] == S2[m]` → `dp[n][m] = dp[n-1][m-1] + 1` (공통 문자 하나 추가)
  - `S1[n] != S2[m]` → `dp[n][m] = max(dp[n-1][m], dp[n][m-1])` (한쪽 문자를 스킵하고 본 결과 중 최댓값)

각 문자열 앞에 공백 한 칸을 패딩해 1-indexed로 다루면 `dp[0][*] = dp[*][0] = 0`이 자연스럽게 base case가 됨.

## 풀이

### Solution 1 — Bottom-Up

```python
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dp[n][m]: S1의 n번째까지, S2의 m번째까지 까지 봤을 때 만들 수 있는 LCS

# input
S1 = input().strip()
S2 = input().strip()

# solve
N, M = len(S1), len(S2)
S1 = " " + S1
S2 = " " + S2

dp = [[0] * (M + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for m in range(1, M + 1):
        if S1[n] == S2[m]:
            dp[n][m] = dp[n - 1][m - 1] + 1
        else:
            dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])

print(dp[N][M])
```

- `S1`, `S2` 앞에 공백 패딩 → `S1[1..N]`, `S2[1..M]`로 1-indexed
- `dp`도 `(N+1) × (M+1)`로 잡아 0번 행/열이 자동 base case (0)
- 작은 인덱스부터 차례로 채우는 표준 상향식

### Solution 2 — Top-Down (메모이제이션)

```python
def func(n, m):

    # base case
    if n == 0 or m == 0:
        return 0

    if dp[n][m] != -1:
        return dp[n][m]

    # recursive case
    if S1[n] == S2[m]:
        dp[n][m] = func(n - 1, m - 1) + 1
    else:
        dp[n][m] = max(func(n - 1, m), func(n, m - 1))

    return dp[n][m]


# input
S1 = input().strip()
S2 = input().strip()

# solve
N, M = len(S1), len(S2)
S1 = " " + S1
S2 = " " + S2

dp = [[-1] * (M + 1) for _ in range(N + 1)]

print(func(N, M))
```

- `n == 0 or m == 0`에서 0 반환 → 빈 접두사의 LCS는 0
- 메모 미스(`-1`)일 때만 재귀 → 동일 (n, m)은 한 번만 계산
- `sys.setrecursionlimit(10**6)`으로 깊은 재귀 허용 (최대 N+M ≈ 2000 깊이)

## 복잡도

|            | 시간     | 공간     |
| ---------- | -------- | -------- |
| Solution 1 | O(N × M) | O(N × M) |
| Solution 2 | O(N × M) | O(N × M) |

- N, M ≤ 1000 → 최대 10⁶ 셀, 충분히 통과

## 배운 점

- LCS는 2차원 DP의 대표 예제: 핵심은 **"두 수열을 각각 어디까지 봤는가"** 를 상태로 잡는 것 → (i, j) 2차원 격자 DP
- LCS 얻기 위한 점화식: 문자가 일치하면 **대각선 + 1**, 아니면 **위/왼쪽 중 최대**
- 문자열 앞에 공백/더미 1칸 패딩하면 1-indexed가 되어 `i-1`, `j-1` 경계 체크 없이 점화식이 깔끔
- 경로 복원이 필요하면 `dp` 배열을 역추적하여 실제 LCS 문자열을 구할 수 있음

```python
i, j = N, M
answer = []

while i > 0 and j > 0:
    if S1[i] == S2[j]:
        answer.append(S1[i])
        i -= 1
        j -= 1
    else:
        if dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

answer.reverse()

print("".join(answer))
```
