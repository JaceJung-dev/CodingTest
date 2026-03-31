# 237. Delete Node in a Linked List

## 문제

- 링크: https://leetcode.com/problems/delete-node-in-a-linked-list/
- 난이도: Medium
- 태그: Linked List

## 접근 방식

- head가 주어지지 않고 삭제할 노드만 주어지는 특수한 상황
- 일반적인 "이전 노드의 next를 변경"하는 삭제가 불가능
- 다음 노드의 값을 현재 노드에 복사하고, 다음 노드를 건너뛰어 제거

## 풀이

```python
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
```

## 복잡도

- 시간: O(1) — 상수 연산
- 공간: O(1) — 추가 메모리 없음

## 배운 점

- "노드를 삭제한다"가 반드시 해당 노드를 메모리에서 제거하는 것은 아님 — 값을 덮어쓰는 것도 삭제의 한 방법
- 이 트릭은 tail 노드에는 사용 불가 (next가 없으므로)
