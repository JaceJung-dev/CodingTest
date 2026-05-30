# BOJ 2178 - 미로 탐색

## 문제

- 링크: https://www.acmicpc.net/problem/2178
- 태그: 그래프 이론, 그래프 탐색, 너비 우선 탐색

## 접근 방식

N×M 미로에서 (1,1)부터 (N,M)까지 이동할 때 지나는 최소 칸 수를 구하는 문제. 가중치가 모두 동일한 최단 경로이므로 **BFS**로 해결. 큐에 `(거리, y, x)`를 넣고 처음 도착 지점에 도달했을 때의 거리가 곧 정답.

- 입력 배열을 1-indexed로 패딩하여 경계 검사를 단순화
- `visited` 배열로 재방문 방지 (큐에 넣는 시점에 방문 처리하여 중복 삽입 차단)

## 풀이

```python
import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())
maze = ["0" * (M + 1)] + ["0" + input().strip() for _ in range(N + 1)]
visited = [[False] * (M + 1) for _ in range(N + 1)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue = deque()
queue.append((1, 1, 1))
visited[1][1] = True

while queue:
    dist, y, x = queue.popleft()

    if y == N and x == M:
        print(dist)
        exit()

    for dy, dx in dirs:
        ny, nx = y + dy, x + dx

        if (
            (1 <= ny <= N and 1 <= nx <= M)
            and (not visited[ny][nx])
            and (maze[ny][nx] == "1")
        ):
            queue.append((dist + 1, ny, nx))
            visited[ny][nx] = True
```

- `maze`를 `"0"` 패딩하여 1-indexed로 사용 → 경계 조건 `1 <= ny <= N`만 체크
- 큐에 넣는 시점에 `visited = True` 처리 → 같은 칸이 큐에 여러 번 쌓이는 것을 방지
- 도착하는 순간 `dist` 출력 후 즉시 종료

## 복잡도

| | 시간 | 공간 |
| --- | --- | --- |
| BFS | O(N × M) | O(N × M) |

## 배운 점

- BFS는 가중치가 모두 같은 그래프에서 **최단 경로 = 최소 간선 수**를 보장
- 방문 처리는 **큐에서 꺼낼 때**가 아니라 **큐에 넣을 때** 하는 게 안전 (중복 삽입 방지, 메모리/시간 모두 이득)
- 1-indexed 패딩은 경계 검사 로직을 깔끔하게 만드는 관용적 트릭
