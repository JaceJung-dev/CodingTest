# 104. Maximum Depth of Binary Tree

## 문제

- 링크: https://leetcode.com/problems/maximum-depth-of-binary-tree/
- 난이도: Easy
- 태그: Tree, Depth-First-Search(DFS), Breadth-First-Search(BFS), Binary Tree

## 접근 방식

### Solution 1 — DFS (재귀)

- 빈 노드면 0 반환
- 왼쪽/오른쪽 서브트리의 깊이 중 큰 값에 +1

### Solution 2 — BFS (레벨 순회)

- deque로 레벨 단위 순회
- 한 레벨을 처리할 때마다 depth +1
- 큐가 비면 모든 레벨 탐색 완료

## 풀이

### Solution 1

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

### Solution 2

```python
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append(root)
        depth = 0

        while q:
            depth += 1

            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth
```

## 복잡도

|            | 시간 | 공간                               |
| ---------- | ---- | ---------------------------------- |
| Solution 1 | O(n) | O(h) — 재귀 스택 (h: 트리 높이)    |
| Solution 2 | O(n) | O(w) — 큐 크기 (w: 가장 넓은 레벨) |

## 배운 점

- DFS 재귀는 트리 문제의 가장 기본적인 패턴 — base case + 재귀 호출 + 결합
- BFS 레벨 순회에서 `for _ in range(len(q))`로 레벨 단위 처리하는 것이 핵심 관용 표현
- 균형 트리면 DFS가 O(log n) 공간, 편향 트리면 O(n) — BFS는 반대
