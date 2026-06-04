# BOJ 1753 - 최단경로

## 문제

- 링크: https://www.acmicpc.net/problem/1753
- 태그: 그래프 이론, 데이크스트라, 최단 경로

## 접근 방식

방향 그래프에서 시작 정점 K로부터 모든 정점까지의 최단 경로를 구하는 문제. 간선 가중치가 양수(1~10)이므로 **우선순위 큐 기반 다익스트라(Dijkstra)** 알고리즘으로 해결.

- `dist[v]`: K에서 v까지의 현재까지 알려진 최단 거리 (초기값 INF, `dist[K] = 0`)
- 힙에서 가장 가까운 정점을 꺼내, 인접 정점을 통한 거리 갱신 시도
- 이미 더 짧은 경로로 처리된 항목은 **lazy deletion** 패턴으로 스킵 (`cur_dist > dist[cur_node]`)

## 풀이

```python
import heapq
import sys

input = sys.stdin.readline

INF = 10**12

# input
V, E = map(int, input().split())
K = int(input())
adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    s, e, d = map(int, input().split())
    adj_list[s].append((e, d))

# solve
dist = [INF] * (V + 1)
dist[K] = 0

heap = []
heapq.heappush(heap, (0, K))  # (dist, node)

while heap:
    cur_dist, cur_node = heapq.heappop(heap)

    if cur_dist > dist[cur_node]:
        continue

    for adj_node, adj_dist in adj_list[cur_node]:
        temp_dist = cur_dist + adj_dist

        if temp_dist < dist[adj_node]:
            dist[adj_node] = temp_dist
            heapq.heappush(heap, (temp_dist, adj_node))

for d in dist[1:]:
    print(d if not d == INF else "INF")
```

- 인접 리스트(`adj_list`)로 그래프를 표현 → 간선이 많아도 공간 효율적
- 힙 튜플은 `(거리, 노드)` 순서여야 거리 기준으로 정렬됨
- `cur_dist > dist[cur_node]` 체크: 같은 노드가 힙에 여러 번 들어갔을 때 **한 번만 유효 처리**
- 출력은 정점 1부터 V까지, INF는 `"INF"` 문자열로 치환

## 복잡도

|               | 시간             | 공간     |
| ------------- | ---------------- | -------- |
| Dijkstra (힙) | O((V + E) log V) | O(V + E) |

- V ≤ 20,000, E ≤ 300,000 → 약 3×10⁵ × log(2×10⁴) ≈ 5×10⁶ 연산

## 배운 점

- 양의 가중치 단일 시작점 최단 경로의 표준 해법은 **힙 기반 다익스트라**
- `visited` 배열 대신 `cur_dist > dist[cur_node]`로 중복 처리를 걸러내는 방식(lazy deletion)이 파이썬 `heapq`와 잘 맞음 (`heapq`는 decrease-key가 없어서 새 튜플을 push하고 오래된 건 스킵)
- 힙 튜플에서 정렬 키를 **앞쪽**에 배치하는 관용 (`(거리, 노드)`)
