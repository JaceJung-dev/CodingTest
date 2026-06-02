# BOJ 7576 - 토마토

## 문제

- 링크: https://www.acmicpc.net/problem/7576
- 태그: 그래프 이론, 그래프 탐색, 너비 우선 탐색

## 접근 방식

모든 익은 토마토(`1`)가 동시에 하루에 한 칸씩 퍼지며 덜 익은 토마토(`0`)를 익히는 문제. 모든 익은 토마토를 **초기 큐**에 넣고 BFS를 돌리는 **다중 시작점 BFS (Multi-source BFS)** 로 해결.

- `time[y][x]`: 해당 칸이 익는 데 걸리는 일수 (초기값 INF)
- 모든 `1` 칸을 큐에 넣고 `time = 0`으로 시작
- 정답은 `-1`이 아닌 칸들의 `time` 최댓값 → INF가 남아있으면 `-1` 출력

## 풀이

```python
import sys
from collections import deque

INF = 10**12

input = sys.stdin.readline

# input
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# solve
queue = deque()
time = [[INF] * M for _ in range(N)]

for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            queue.append((y, x))
            time[y][x] = 0

while queue:
    y, x = queue.popleft()

    nxts = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]

    for ny, nx in nxts:
        if not (0 <= ny < N and 0 <= nx < M):
            continue

        if time[ny][nx] <= time[y][x] + 1:
            continue

        if matrix[ny][nx] == -1:
            continue

        queue.append((ny, nx))
        time[ny][nx] = time[y][x] + 1

ans = -1
for y in range(N):
    for x in range(M):
        if matrix[y][x] != -1:
            ans = max(ans, time[y][x])

print(ans if ans != INF else -1)
```

- 익은 토마토를 **모두** 큐에 동시에 넣는 게 핵심 → 시작점이 여러 개여도 BFS의 레이어 확장이 동기화됨
- `time[ny][nx] <= time[y][x] + 1` 체크는 `visited` 역할 + 더 빠른 경로가 이미 있으면 스킵
- 마지막에 `-1`이 아닌 칸을 스캔하여 최댓값 → 그 값이 INF면 덜 익은 토마토가 남은 것

## 복잡도

| | 시간 | 공간 |
| --- | --- | --- |
| Multi-source BFS | O(N × M) | O(N × M) |

- N, M ≤ 1,000 → 최대 10⁶ 칸

## 배운 점

- 여러 시작점에서 동시에 퍼지는 탐색은 **초기 큐에 전부 넣고 한 번의 BFS**로 처리 (각각 따로 돌리면 비효율)
- `visited` 대신 `time[] = INF`로 초기화하고 거리 배열 자체가 방문 체크 역할을 겸할 수 있음
- "모두 익는 최소 일수" = BFS 완료 후 거리 배열의 최댓값, "못 익는 칸" = 거리 배열에 INF가 남음
