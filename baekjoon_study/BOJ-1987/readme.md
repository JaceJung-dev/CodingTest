# BOJ 1987 - 알파벳

## 문제

- 링크: https://www.acmicpc.net/problem/1987
- 태그: 그래프 이론, 그래프 탐색, 백트래킹, DFS

## 접근 방식

좌상단 (0, 0)에서 출발해 상하좌우로 이동하되 **이미 지나온 알파벳은 다시 방문할 수 없다**. 지날 수 있는 최대 칸 수를 구하는 문제.

- 격자 위 백트래킹: 한 경로를 끝까지 따라간 뒤 **상태를 원복**하고 다른 가지로 이동
- "방문" 단위가 좌표가 아니라 **알파벳**이라는 점이 핵심 → 좌표별 visited 배열이 아니라 **사용한 알파벳 집합**을 들고 다녀야 함
- R, C ≤ 20, 알파벳은 26자 → 한 경로의 최대 길이는 26으로 제한됨 → 백트래킹이 충분

## 풀이

### Solution 1 — `set`으로 사용한 알파벳 추적

```python
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def search(y, x):
    global cnt

    if y < 0 or x < 0 or y >= R or x >= C:
        return

    if matrix[y][x] in seen:
        return

    seen.add(matrix[y][x])

    cnt = max(cnt, len(seen))

    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx

        search(ny, nx)

    seen.remove(matrix[y][x])


# input
R, C = map(int, input().split())
matrix = [input().strip() for _ in range(R)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
seen = set()
cnt = 0

search(0, 0)

print(cnt)
```

- `seen` 집합에 현재 경로에서 지나온 알파벳을 담음
- 진입 시 `add`, 4방향 재귀 후 **`remove`로 원복** → 백트래킹의 핵심
- 정답은 `len(seen)`의 최댓값

### Solution 2 — `bool` 배열(26칸) + 길이 카운터

```python
def search(y, x):
    global cnt, cur_len

    if y < 0 or x < 0 or y >= R or x >= C:
        return
    if check[ord(matrix[y][x]) - ord("A")]:
        return

    check[ord(matrix[y][x]) - ord("A")] = True
    cur_len += 1

    cnt = max(cnt, cur_len)

    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx

        search(ny, nx)

    cur_len -= 1
    check[ord(matrix[y][x]) - ord("A")] = False


# input
R, C = map(int, input().split())
matrix = [input().strip() for _ in range(R)]

# solve
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
check = [False] * 26
cnt = 0
cur_len = 0

search(0, 0)

print(cnt)
```

- `set` 대신 길이 26의 `bool` 배열로 사용 여부 관리 → 해시 비용 제거
- `len(seen)` 호출도 빼고 `cur_len` 카운터를 같이 +/-로 갱신 → 상수 시간 비교
- 알고리즘은 동일하나 상수가 작아 더 빠름

## 복잡도

| | 시간 | 공간 |
| --- | --- | --- |
| Solution 1 | O(4^L), L ≤ 26 | O(L) (set + 재귀) |
| Solution 2 | O(4^L), L ≤ 26 | O(L) (배열은 상수) |

- 알파벳이 26자뿐이라 한 경로의 길이가 최대 26으로 제한됨 → 가지치기가 자연스럽게 발생

## 배운 점

- "지나온 X를 두 번 못 쓴다" 류 백트래킹은 **상태를 들고 들어가서 원복하는 패턴**이 정석: `상태 갱신 → 재귀 → 상태 복구`
- 좌표 기반 visited(2D 배열)와 **값 기반 visited(알파벳 집합)** 는 다른 자료구조 → 문제의 "중복 금지" 조건이 무엇에 걸려 있는지 정확히 읽어야 함
- `set` ↔ 길이 고정 `bool` 배열 변환은 흔한 상수 최적화 (도메인이 작을 때 특히 유효): 해시 비용 제거 + 캐시 친화적
- `len(set)`을 매번 호출하지 않고 별도 카운터를 유지하면 호출 비용을 한 번 더 줄일 수 있음
