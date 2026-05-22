# BOJ 2580 - 스도쿠

## 문제

- 링크: https://www.acmicpc.net/problem/2580
- 태그: 백트래킹, 브루트포스 알고리즘

## 접근 방식

9×9 보드의 빈 칸(0)을 1~9로 채워 스도쿠를 완성하는 문제. 빈 칸에 숫자를 하나씩 시도하며 **행/열/3×3 박스에 같은 수가 없는지** 확인하는 백트래킹.

- 빈 칸 좌표를 미리 모아 `pos` 리스트로 만들고, `level` 인덱스로 한 칸씩 채워 나감
- `level == len(pos)`이면 해 발견 → 보드 출력 후 즉시 종료
- 검사 방식에 따라 세 가지 풀이로 정리

## 풀이

### Solution 1 — 매 시도마다 행/열/박스 스캔

```python
import sys

input = sys.stdin.readline


# Solution 1
def is_possible(y, x, n):

    for i in range(9):
        if matrix[i][x] == n:
            return False

    for j in range(9):
        if matrix[y][j] == n:
            return False

    for i in range(3):
        for j in range(3):
            if matrix[3 * (y // 3) + i][3 * (x // 3) + j] == n:
                return False

    return True


def search(level):
    # base case
    if level == len(pos):
        for row in matrix:
            print(*row)
        sys.exit(0)

    y, x = pos[level]

    # recursive case
    for n in range(1, 10):
        if is_possible(y, x, n):
            matrix[y][x] = n
            search(level + 1)
            matrix[y][x] = 0


# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
pos = []
for i in range(9):
    for j in range(9):
        if matrix[i][j] == 0:
            pos.append((i, j))

search(0)
```

- 매번 `is_possible`이 O(9 + 9 + 9) = O(27) 검사 → 빈 칸 수 × 9 × 27 만큼 일이 늘어남
- 이해/구현이 가장 단순

### Solution 2 — 행/열/박스에 `set`을 미리 유지

```python
def search(level):

    # base case
    if level == len(pos):
        for row in matrix:
            print(*row)
        sys.exit(0)

    y, x = pos[level]

    # recursive case
    for n in range(1, 10):
        if n not in rows[y] and n not in cols[x] and n not in squares[y // 3][x // 3]:
            matrix[y][x] = n
            rows[y].add(n)
            cols[x].add(n)
            squares[y // 3][x // 3].add(n)

            search(level + 1)

            matrix[y][x] = 0
            rows[y].remove(n)
            cols[x].remove(n)
            squares[y // 3][x // 3].remove(n)


# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
squares = [[set() for _ in range(3)] for _ in range(3)]

pos = []
for i in range(9):
    for j in range(9):
        cur = matrix[i][j]
        if cur == 0:
            pos.append((i, j))
        else:
            rows[i].add(cur)
            cols[j].add(cur)
            squares[i // 3][j // 3].add(cur)

search(0)
```

- 입력 시 미리 사용 중인 숫자를 `rows`, `cols`, `squares`에 등록 → 검사 비용을 O(1)로 줄임
- 진입할 때 등록, 백트래킹할 때 제거 (`add` ↔ `remove`)
- 정답 후보 가지치기가 자연스럽게 빨라짐

### Solution 3 — `bool` 배열(10칸)로 사용 여부 관리

```python
def search(level):

    # base case
    if level == len(pos):
        for row in matrix:
            print(*row)
        sys.exit(0)

    y, x = pos[level]

    # recursive case
    for n in range(1, 10):
        if not rows[y][n] and not cols[x][n] and not squares[y // 3][x // 3][n]:
            matrix[y][x] = n
            rows[y][n] = True
            cols[x][n] = True
            squares[y // 3][x // 3][n] = True

            search(level + 1)

            matrix[y][x] = 0
            rows[y][n] = False
            cols[x][n] = False
            squares[y // 3][x // 3][n] = False


# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
rows = [[False] * 10 for _ in range(9)]
cols = [[False] * 10 for _ in range(9)]
squares = [[[False] * 10 for _ in range(3)] for _ in range(3)]
pos = []

for i in range(9):
    for j in range(9):
        cur = matrix[i][j]
        if cur == 0:
            pos.append((i, j))
        else:
            rows[i][cur] = True
            cols[j][cur] = True
            squares[i // 3][j // 3][cur] = True

search(0)
```

- `set` 대신 길이 10의 `bool` 배열로 in/out 검사 → 해시 비용 제거
- 도메인이 1~9로 작을 때 자주 쓰는 상수 최적화
- 알고리즘은 Solution 2와 동일

## 복잡도

- 백트래킹의 정확한 worst-case는 정의하기 까다롭지만, 빈 칸 수를 K라 하면 최악 O(9^K) 이하
- 실전적으로는 행/열/박스 가지치기 덕분에 훨씬 빠르게 끝남

|            | 검사 비용         | 메모리                       |
| ---------- | ----------------- | ---------------------------- |
| Solution 1 | 시도당 O(27)      | O(1) 보조                    |
| Solution 2 | 시도당 O(1) (set) | O(81) 보조                   |
| Solution 3 | 시도당 O(1) (배열)| O(81) 보조, 상수 더 작음     |

## 배운 점

- "한 칸씩 채우다가 막히면 되돌리기" → 스도쿠/N-Queens 류의 정석 백트래킹 구조
- 빈 칸 좌표를 미리 모아 `level` 인덱스로 진행하면 중첩 좌표 순회 대신 **선형 진행**이 되어 코드가 깔끔
- "조건을 매번 스캔" → "사용 여부를 미리 유지" 로 바꾸면 시도당 검사 비용이 O(N) → O(1)
- 도메인이 작으면(1~9) `set` 대신 길이 고정 `bool` 배열로 한 단계 더 최적화 가능
- 해를 찾자마자 즉시 종료해야 함 → `sys.exit(0)` 또는 플래그로 모든 재귀를 빠져나오는 패턴
