# BOJ 2606 - 바이러스

## 문제

- 링크: https://www.acmicpc.net/problem/2606
- 태그: 그래프, DFS, BFS

## 접근 방식

네트워크에서 1번 컴퓨터로부터 바이러스가 전파될 수 있는 컴퓨터 수를 구하는 문제. 1번 정점에서 시작하는 그래프 탐색으로 도달 가능한 정점 수를 세고, 1번 자신을 제외하기 위해 `-1`. 두 가지 방식으로 구현:

1. **DFS (재귀)** - 1번에서 재귀 탐색
2. **BFS (큐)** - 1번에서 너비 우선 탐색

## 풀이

### Solution 1 — DFS (재귀)

```python
def solve_dfs(snode):
    global visited, count

    if visited[snode]:
        return

    visited[snode] = True
    count += 1

    for adj_node in adj_list[snode]:
        solve_dfs(adj_node)
```

- 방문 체크 → 카운트 증가 → 인접 노드 재귀 호출

### Solution 2 — BFS (큐)

```python
def solve_bfs(node):
    global visited, count
    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue:
        cur_node = queue.popleft()

        count += 1

        for adj_node in adj_list[cur_node]:
            if not visited[adj_node]:
                queue.append(adj_node)
                visited[adj_node] = True
```

- push 시점에 방문 처리하여 중복 큐잉 방지
- pop할 때마다 카운트 증가

### 공통

- 인접 리스트로 그래프 구성 (양방향)
- 1번에서 시작한 후 `count - 1` 출력 (1번 자신은 감염 대상이 아님)

## 복잡도

- 시간: O(V + E) — 각 정점/간선 한 번씩 방문
- 공간: O(V + E) — 인접 리스트, visited 배열, 스택/큐

## 배운 점

- 연결 요소 크기를 구하는 기본 문제: DFS/BFS 둘 다 동일하게 동작
- 시작 정점을 제외해야 할 때는 `count - 1`처럼 후처리로 간단히 해결
- 1260번과 동일한 탐색 골격을 재사용 — 순회 문제의 템플릿을 익히는 데 유용
