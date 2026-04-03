# 206. Reverse Linked List

## 문제

- 링크: https://leetcode.com/problems/reverse-linked-list/
- 난이도: Easy
- 태그: Linked List, Recursion

## 접근 방식

### Solution 1 — 반복 (Iterative)

- prev, curr 두 포인터로 순회하며 화살표 방향을 뒤집음
- `curr.next`를 prev로 바꾸기 전에 temp에 다음 노드를 저장

### Solution 2 — 재귀 (Recursive)

- 끝까지 재귀로 들어가서 new_head(마지막 노드)를 잡고
- 돌아오면서 `head.next.next = head`로 역방향 연결, `head.next = None`으로 기존 연결 끊기

## 풀이

### Solution 1

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
```

### Solution 2

```python
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
```

## 복잡도

|            | 시간 | 공간                       |
| ---------- | ---- | -------------------------- |
| Solution 1 | O(n) | O(1) — 포인터만 사용       |
| Solution 2 | O(n) | O(n) — 재귀 호출 스택 깊이 |

## 배운 점

- 반복 풀이의 핵심은 `temp → 방향 전환 → prev 이동 → curr 이동` 4단계 순서
- 재귀 풀이는 `head.next.next = head`가 역방향 연결의 핵심 (그림 그리기)
