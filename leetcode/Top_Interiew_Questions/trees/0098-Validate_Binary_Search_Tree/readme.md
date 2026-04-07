# 98. Validate Binary Search Tree

## 문제

- 링크: https://leetcode.com/problems/validate-binary-search-tree/
- 난이도: Medium
- 태그: Tree, Depth-First-Search(DFS), Binary Search Tree, Binary Tree

## 접근 방식

- 각 노드가 허용 범위(minimum, maximum) 안에 있는지 재귀적으로 검증
- 왼쪽 서브트리로 내려갈 때 maximum을 현재 노드 값으로 갱신
- 오른쪽 서브트리로 내려갈 때 minimum을 현재 노드 값으로 갱신
- 초기 범위는 `(-inf, inf)`

## 풀이

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, minimum, maximum):
            if not node:
                return True

            if not minimum < node.val < maximum:
                return False

            return validate(node.left, minimum, node.val) and validate(
                node.right, node.val, maximum
            )

        return validate(root, float("-inf"), float("inf"))
```

## 복잡도

- 시간: O(n) — 모든 노드를 한 번씩 방문
- 공간: O(h) — 재귀 스택 (h: 트리 높이)

## 배운 점

- BST 검증에서 흔한 실수: 왼쪽 자식 < 부모만 체크하면 안 됨 — 조상 노드의 범위까지 고려해야 함
- 범위를 파라미터로 내려보내는 top-down 패턴이 이를 자연스럽게 해결
- 중위 순회(inorder)로 풀 수도 있음 — BST의 inorder 결과는 항상 오름차순
