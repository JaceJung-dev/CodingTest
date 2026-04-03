# 141. Linked List Cycle

## 문제

- 링크: https://leetcode.com/problems/linked-list-cycle/
- 난이도: Easy
- 태그: Linked List, Two Pointers

## 접근 방식

- Floyd's Cycle Detection (토끼와 거북이)
- fast는 2칸, slow는 1칸씩 이동
- 사이클이 있으면 fast가 slow를 따라잡아 반드시 만남
- 사이클이 없으면 fast가 끝에 도달하여 루프 종료

## 풀이

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
```

## 복잡도

- 시간: O(n) — 사이클이 있으면 fast가 slow를 한 바퀴 안에 따라잡음
- 공간: O(1) — 포인터 두 개만 사용

## 배운 점

- Floyd's Cycle Detection은 사이클 판별의 표준 알고리즘
- set으로 방문 노드를 저장하면 O(n) 공간이 필요하지만, fast/slow는 O(1)로 해결
- 142번(Linked List Cycle II)에서는 사이클 시작점도 찾을 수 있음
