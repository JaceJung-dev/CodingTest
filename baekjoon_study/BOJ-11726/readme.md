# BOJ 11726 - 2×n 타일링

## 문제

- 링크: https://www.acmicpc.net/problem/11726
- 태그: 다이나믹 프로그래밍

## 접근 방식

2×n 직사각형을 1×2, 2×1 타일로 채우는 경우의 수. 마지막 칸을 채우는 방식에 따라 두 가지로 나뉜다:

- 맨 오른쪽에 **2×1 세로 타일 1개** → 남은 영역은 2×(n-1) → `dp[n-1]`
- 맨 오른쪽에 **1×2 가로 타일 2개** (2칸 세로로 쌓임) → 남은 영역은 2×(n-2) → `dp[n-2]`

따라서 점화식:

```
dp[n] = dp[n-1] + dp[n-2]   (mod 10007)
dp[1] = 1, dp[2] = 2
```

피보나치와 동일한 형태. n ≤ 1000이므로 O(N) DP면 충분.

## 풀이

### Solution 1 — O(1) 공간 (변수 두 개로 갱신)

```python
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2

    for _ in range(2, n):
        a, b = b, (a + b) % 10007

    return b


# input
N = int(input())

# solve
print(func(N))
```

- `a`, `b` 두 변수만 유지하며 `(a, b) = (b, a+b)`로 미끄러뜨림
- 공간 O(1)

### Solution 2 — Bottom-Up (반복 + 배열)

```python
# input
N = int(input())

# solve
dp = [0] * (N + 2)
dp[1], dp[2] = 1, 2

for n in range(3, N + 1):
    dp[n] = (dp[n - 1] + dp[n - 2]) % 10007

print(dp[N])
```

- 표준적인 DP 테이블 채우기. `dp[N + 2]` 크기로 잡아 N=1, N=2의 경계도 안전하게 처리

### Solution 3 — Top-Down (메모이제이션)

```python
def func(n):

    # base case
    if n == 1 or n == 2:
        return n

    if dp[n] != -1:
        return dp[n]

    # recursive case
    dp[n] = (func(n - 1) + func(n - 2)) % 10007

    return dp[n]


# input
N = int(input())

# solve
dp = [-1] * (N + 1)

print(func(N))
```

- 메모 미스(`-1`)일 때만 재귀 → 동일 인덱스는 한 번만 계산
- `sys.setrecursionlimit(10**6)`으로 깊은 재귀 허용

## 복잡도

| | 시간 | 공간 |
| --- | --- | --- |
| Solution 1 | O(N) | O(1) |
| Solution 2 | O(N) | O(N) |
| Solution 3 | O(N) | O(N) |

## 배운 점

- "마지막 칸/마지막 단계를 어떻게 채울지"로 케이스를 나누면 자연스럽게 점화식이 도출됨 → 타일링 문제의 정석 접근
- 2×n 타일링은 **피보나치 수열과 동일**한 점화식: `dp[n] = dp[n-1] + dp[n-2]`
- 모듈러 연산은 매 단계마다 적용해도 결과 동일 → 큰 수 오버플로 걱정 없음 (Python은 무관하지만 습관)
- 동일 점화식을 세 가지 스타일(O(1) 슬라이딩, 상향식 배열, 하향식 메모)로 풀어보면 DP 사고가 단단해짐
