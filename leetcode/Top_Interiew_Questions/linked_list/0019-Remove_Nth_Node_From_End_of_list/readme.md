# 19. Remove Nth Node From End of List

## 문제

- 링크: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- 난이도: Medium
- 태그: Linked List, Two Pointers

## 접근 방식

### Solution 1 — Dummy Node + Fast/Slow

- dummy 노드를 앞에 붙여 head 삭제 케이스를 일반화
- fast를 n칸 먼저 이동 → 이후 fast와 slow를 동시에 이동
- fast가 끝에 도달하면 slow가 삭제 대상의 이전 노드에 위치

### Solution 2 — Dummy Node 없이

- fast를 n칸 먼저 이동 후, fast가 None이면 head 자체를 삭제하는 경우 → `head.next` 반환
- 그 외에는 동시 이동 후 삭제

## 풀이

### Solution 1

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
```

### Solution 2

```python
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
```

## 복잡도

- 시간: O(n) — 리스트를 한 번 순회 (둘 다 동일)
- 공간: O(1) — 포인터만 사용 (둘 다 동일)

## 배운 점

- fast/slow 포인터 간격을 n으로 유지하면 한 번의 순회로 "끝에서 n번째"를 찾을 수 있음
- dummy 노드를 사용하면 head 삭제 같은 엣지 케이스를 별도 처리 없이 통합 가능
- Solution 2는 dummy 없이 `if not fast` 분기로 head 삭제를 직접 처리
