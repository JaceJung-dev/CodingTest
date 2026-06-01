# BOJ 2468 - 안전 영역

## 문제

- 링크: https://www.acmicpc.net/problem/2468
- 태그: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 브루트포스

## 접근 방식

비의 높이 `h`에 따라 잠기지 않는 칸(`matrix[y][x] > h`)들의 **연결 요소(Connected Component) 개수**를 구하고, 모든 가능한 `h`에 대해 최댓값을 찾는 문제.

- 높이 범위가 1~100으로 작음 → 각 `h = 0..100`에 대해 전체 격자를 탐색해도 `O(101 × N²)`로 충분
- 각 `h`에서 미방문이면서 잠기지 않은 칸을 시작점으로 DFS/BFS → 방문 표시, 컴포넌트 수 카운트

## 풀이

### Solution 1 — DFS (재귀)

```python
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


# Solution 1
def dfs(sy, sx, height):

    if not (0 <= sy < N and 0 <= sx < N):
        return

    if visited[sy][sx] or (matrix[sy][sx] <= height):
        return

    visited[sy][sx] = True

    for dy, dx in dirs:
        ny, nx = sy + dy, sx + dx
        dfs(ny, nx, height)


def get_count(height):
    global visited

    visited = [[False] * N for _ in range(N)]

    count = 0
    for y in range(N):
        for x in range(N):
            if (not visited[y][x]) and (matrix[y][x] > height):
                dfs(y, x, height)
                count += 1
    return count


# input
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

max_count = 0
for h in range(101):
    max_count = max(max_count, get_count(h))

print(max_count)
```

- 재귀 DFS에서 경계/방문/잠김 체크를 함수 진입부에서 수행 → 호출 부담은 있으나 코드가 간결
- N이 최대 100이라 재귀 깊이 최악 10,000 → `setrecursionlimit` 필요
- `dfs`는 인자 `height`를 끝까지 일관되게 사용 (전역 `h`에 의존하지 않음)

### Solution 2 — BFS (큐)

```python
from collections import deque


# Solution 2
def bfs(sy, sx, height):
    queue = deque()
    queue.append((sy, sx))
    visited[sy][sx] = True

    while queue:
        y, x = queue.popleft()

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if (
                (0 <= nx < N and 0 <= ny < N)
                and (not visited[ny][nx])
                and (matrix[ny][nx] > height)
            ):
                queue.append((ny, nx))
                visited[ny][nx] = True


def get_count(height):
    global visited

    visited = [[False] * N for _ in range(N)]

    count = 0
    for y in range(N):
        for x in range(N):
            if (not visited[y][x]) and (matrix[y][x] > height):
                bfs(y, x, height)
                count += 1

    return count


# input
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

max_count = 0
for h in range(101):
    max_count = max(max_count, get_count(h))

print(max_count)
```

- 큐 기반 BFS → 재귀 깊이 문제 없음
- 시작 칸은 push 시점에 방문 표시 (Solution 1과 동일하게 시작 칸의 잠김 여부는 `get_count`에서 사전 검증)
- `get_count` 로직은 DFS 버전과 동일, 탐색 함수만 교체

## 복잡도

|           | 시간      | 공간  |
| --------- | --------- | ----- |
| DFS / BFS | O(H × N²) | O(N²) |

- H = 100 (높이 범위), N ≤ 100 → 최대 약 100 × 10,000 = 10⁶ 연산

## 배운 점

- "조건에 따른 연결 요소 개수"는 **DFS/BFS로 전체를 훑으며 시작점 카운트**하는 전형적 패턴
- 값 범위가 작으면 모든 임계값에 대해 브루트포스로 반복해도 충분 (이 문제에선 h=0..100)
- 재귀 DFS는 `setrecursionlimit`이 필수, 큐 BFS는 메모리가 좀 더 들지만 안전
- 매개변수와 전역 변수가 같은 이름/같은 값을 갖더라도 함수 본문에서는 **매개변수만 참조하도록 일관성 유지** — 호출 컨텍스트가 바뀌어도 안전하게 동작
