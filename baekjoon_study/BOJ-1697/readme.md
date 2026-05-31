# BOJ 1697 - 숨바꼭질

## 문제

- 링크: https://www.acmicpc.net/problem/1697
- 태그: 그래프 이론, 그래프 탐색, 너비 우선 탐색

## 접근 방식

수빈(N) → 동생(M)까지 `X-1`, `X+1`, `X*2` 세 가지 이동을 1초에 한 번씩 할 때 최소 시간을 구하는 문제. 각 이동의 비용이 모두 1초로 동일하므로 **BFS**로 최단 시간을 보장.

- 위치 범위 `0 ~ 100,000`을 정점으로 하고, 세 종류의 이동을 간선으로 보는 **암시적 그래프 탐색**
- `visited`로 재방문 차단 (큐 삽입 시점에 처리)

## 풀이

```python
import sys
from collections import deque

input = sys.stdin.readline

MAX = 10**5

# input
N, M = map(int, input().split())

# solve
queue = deque()
visited = [False] * (MAX + 1)

queue.append((0, N))
visited[N] = True

while queue:
    time, pos = queue.popleft()

    if pos == M:
        print(time)
        sys.exit(0)

    for nxt_pos in [pos - 1, pos + 1, pos * 2]:
        if (0 <= nxt_pos <= MAX) and (not visited[nxt_pos]):
            queue.append((time + 1, nxt_pos))
            visited[nxt_pos] = True
```

- 큐에 `(시간, 위치)`를 저장하며 BFS 진행
- 세 가지 다음 위치 후보를 모두 큐에 넣되, 범위(`0 ~ MAX`) 안이고 미방문일 때만 삽입
- 위치가 M과 일치하는 순간의 `time`이 정답

## 복잡도

|     | 시간   | 공간   |
| --- | ------ | ------ |
| BFS | O(MAX) | O(MAX) |

- MAX = 100,000 (위치 범위)

## 배운 점

- 명시적 그래프가 없어도, **상태 = 정점 / 상태 전이 = 간선**으로 보면 BFS/DFS를 그대로 적용 가능
- `X*2` 같은 비선형 이동도 BFS 프레임에 자연스럽게 들어감 (각 전이 비용이 동일하기만 하면 OK)
- 범위 상한을 `MAX`로 고정해 `visited` 배열 크기를 제한하는 게 핵심 (목표 M 이후의 위치는 `X-1`로만 돌아올 수 있으므로 MAX까지만 탐색해도 충분)
