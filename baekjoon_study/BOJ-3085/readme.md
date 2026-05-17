# BOJ 3085 - 사탕 게임

## 문제

- 링크: https://www.acmicpc.net/problem/3085
- 태그: 브루트포스 알고리즘

## 접근 방식

N×N 보드에서 인접한 두 칸을 한 번 교환했을 때 만들 수 있는 "같은 색 연속 행/열의 최대 길이"를 구하는 문제. N ≤ 50으로 작아 **모든 인접 쌍 교환을 시도**해도 충분.

- 시도할 교환의 수: `O(N²)` 칸 × 4방향 = `O(N²)`
- 각 교환마다 행/열 스캔: `O(N²)` (Solution 1) 또는 영향받은 행+열만 `O(N)` (Solution 2)

## 풀이

### Solution 1 — 매 교환마다 전체 보드 스캔

```python
import sys

input = sys.stdin.readline


def get_best():
    best = 0

    # rows
    for i in range(N):
        value = 0
        prev = "-"
        for j in range(N):
            if matrix[i][j] == prev:
                value += 1
            else:
                value = 1
            best = max(best, value)
            prev = matrix[i][j]

    # column
    for j in range(N):
        value = 0
        prev = "-"
        for i in range(N):
            if matrix[i][j] == prev:
                value += 1
            else:
                value = 1
            best = max(best, value)
            prev = matrix[i][j]

    return best


# input
N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

best = 0
for y in range(N):
    for x in range(N):
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N:
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
                best = max(best, get_best())
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]

print(best)
```

- 각 칸 `(y, x)`에서 4방향 인접 칸과 swap → 전체 보드 스캔 → swap-back으로 원상복구
- `get_best()`는 매번 보드 전체의 행/열을 처음부터 다시 훑음 → O(N²)
- 같은 색끼리도 swap을 시도하지만, 같은 값끼리의 swap은 no-op이라 결과에 영향 없음

### Solution 2 — 교환 후 영향받은 행/열만 스캔

```python
def get_best(y, x):
    best = 0

    # row
    value = 0
    prev = "-"
    for j in range(N):
        if matrix[y][j] == prev:
            value += 1
        else:
            value = 1
        best = max(best, value)
        prev = matrix[y][j]

    # column
    value = 0
    prev = "-"
    for i in range(N):
        if matrix[i][x] == prev:
            value += 1
        else:
            value = 1
        best = max(best, value)
        prev = matrix[i][x]

    return best


# input
N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

best = 0
for y in range(N):
    for x in range(N):

        if y == x:
            best = max(best, get_best(y, x))

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N:
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
                best = max(best, get_best(y, x))
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]

print(best)
```

- 인접 두 칸을 교환하면 **두 칸이 속한 행과 열만** 변할 수 있음 → `(y, x)` 기준 행/열만 스캔
- `(ny, nx)`가 속한 행/열도 영향받지만, 어차피 모든 칸 `(y, x)`을 순회하므로 짝의 위치도 다른 시점에 스캔됨
- `if y == x`로 교환 없는 초기 보드도 한 번 평가 (대각선 칸을 만날 때마다 1번씩 → 사실 한 번이면 충분하지만 결과는 동일)

## 복잡도

|            | 시간  | 공간  |
| ---------- | ----- | ----- |
| Solution 1 | O(N⁵) | O(N²) |
| Solution 2 | O(N⁴) | O(N²) |

- N ≤ 50 → Solution 1도 약 3×10⁸로 빡빡하나 통과 가능, Solution 2는 여유

## 배운 점

- 작은 N의 격자 + "한 번의 변형 후 결과" 문제는 **모든 가능한 변형을 시도**하는 브루트포스가 정석
- 교환 시 **swap → 평가 → swap-back** 패턴으로 보드를 매번 복사하지 않고도 원상복구 가능
- 행/열 같은 색 연속 길이 계산은 `prev`와 누적 카운터로 한 번의 선형 스캔이면 충분
- 최적화 포인트: 변경된 행/열만 다시 스캔하면 한 차수 줄일 수 있음 (Solution 2)
