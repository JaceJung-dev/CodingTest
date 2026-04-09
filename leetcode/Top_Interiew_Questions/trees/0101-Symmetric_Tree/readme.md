# 101. Symmetric Tree

## 문제

- 링크: https://leetcode.com/problems/symmetric-tree/
- 난이도: Easy
- 태그: Tree, Depth-First-Search(DFS), Breadth-First-Search(BFS), Binary Tree

## 접근 방식

- 루트의 왼쪽/오른쪽 서브트리가 거울 대칭인지 재귀적으로 검증
- 두 노드가 모두 None이면 대칭 (True)
- 하나만 None이면 비대칭 (False)
- 값이 같으면 `left.left ↔ right.right`, `left.right ↔ right.left` 쌍으로 재귀 비교

## 풀이

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return (
                left.val == right.val
                and is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left)
            )

        return is_mirror(root.left, root.right)
```

## 복잡도

- 시간: O(n) — 모든 노드를 한 번씩 방문
- 공간: O(h) — 재귀 스택 (h: 트리 높이)

## 배운 점

- 대칭 비교는 바깥쪽끼리(`left.left ↔ right.right`), 안쪽끼리(`left.right ↔ right.left`) 비교하는 것
- Same Tree(100번)와 구조가 거의 동일함 (비교 대상 쌍만 다름)
