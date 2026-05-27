# BOJ 1260 - DFS와 BFS

## 문제

- 링크: https://www.acmicpc.net/problem/1260
- 태그: 그래프, DFS, BFS

## 접근 방식

그래프를 인접 리스트로 구성하고 시작 정점 V부터 DFS와 BFS 순회 결과를 출력. 작은 번호부터 방문하기 위해 인접 리스트를 정렬. 세 가지 방식으로 구현:

1. **DFS (재귀)** - 함수 호출 스택을 활용
2. **DFS (스택)** - 명시적 스택으로 반복 구현
3. **BFS (큐)** - `deque`로 FIFO 순회

## 풀이

### Solution 1 — DFS (재귀)

```python
def solve_dfs(node):
    if visited[node]:
        return

    print(node, end=" ")

    visited[node] = True

    for adj_node in adj_list[node]:
        solve_dfs(adj_node)
```

- 방문 체크 → 출력 → 방문 표시 → 인접 노드 재귀 호출

### Solution 2 — DFS (스택)

```python
def solve_stack_dfs(snode):
    stack = []
    stack.append(snode)

    while stack:
        cur_node = stack.pop()
        if visited[cur_node]:
            continue

        visited[cur_node] = True
        print(cur_node, end=" ")

        for adj_node in reversed(adj_list[cur_node]):
            if not visited[adj_node]:
                stack.append(adj_node)
```

- 스택은 LIFO이므로 인접 리스트를 `reversed`로 넣어 작은 번호부터 pop되도록 함
- pop 후 방문 처리(재귀와 달리 중복 push 가능성이 있으므로 방문 체크 필수)

### Solution 3 — BFS (큐)

```python
def solve_bfs(snode):
    queue = deque()
    queue.append(snode)
    visited[snode] = True

    while queue:
        cur_node = queue.popleft()
        print(cur_node, end=" ")

        for adj_node in adj_list[cur_node]:
            if not visited[adj_node]:
                queue.append(adj_node)
                visited[adj_node] = True
```

- `deque.popleft()`로 O(1) 큐 동작
- push 시점에 방문 처리하여 중복 큐잉 방지

### 실행 흐름

```python
import sys
from collections import deque

input = sys.stdin.readline

# input
N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

# solve
for _ in range(M):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

for n in range(1, N + 1):
    adj_list[n].sort()


# Solution 1 (dfs)
visited = [False] * (N + 1)
solve_dfs(V)
print()

# Solution 2 (dfs)
visited = [False] * (N + 1)
solve_stack_dfs(V)
print()

# Solution (bfs)
visited = [False] * (N + 1)
solve_bfs(V)
print()
```

- 인접 리스트를 `sort()`로 정렬하여 작은 번호부터 방문
- 각 순회마다 `visited` 배열을 새로 초기화 → 세 풀이가 같은 그래프 위에서 독립적으로 수행됨

## 복잡도

- 시간: O(V + E) — DFS/BFS 모두 각 정점/간선 한 번씩 방문
- 공간: O(V + E) — 인접 리스트, visited 배열, 스택/큐

## 배운 점

- 재귀 DFS vs 스택 DFS 차이: 스택 DFS는 `reversed`로 순서를 맞춰야 재귀와 동일한 방문 순서가 나옴
- BFS는 push 시점에 방문 처리, DFS(스택)는 pop 시점에 방문 처리하는 게 일반적
  - BFS는 큐에 한 번 들어가면 순서가 고정되지만, DFS(스택)는 나중에 같은 노드가 다시 push될 수 있어서 pop 시 재확인 필요
- 인접 리스트를 미리 정렬하면 각 순회마다 별도의 우선순위 처리 없이 작은 번호 우선 방문 보장
