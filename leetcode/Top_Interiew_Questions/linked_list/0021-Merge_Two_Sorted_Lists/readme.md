# 21. Merge Two Sorted Lists

## 문제

- 링크: https://leetcode.com/problems/merge-two-sorted-lists/
- 난이도: Easy
- 태그: Linked List, Recursion

## 접근 방식

### Solution 1 — 반복 (Iterative)

- dummy 노드를 만들고 curr로 이어 붙이기
- list1, list2 중 작은 값을 curr.next에 연결하며 전진
- 한쪽이 끝나면 나머지를 통째로 연결

### Solution 2 — 재귀 (Recursive)

- 둘 중 작은 쪽을 앞에 놓고, 그 다음부터 재귀적으로 병합
- `list1.val > list2.val`이면 swap하여 항상 list1이 작은 쪽이 되도록 보장

## 풀이

### Solution 1

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next
```

### Solution 2

```python
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        if list1.val > list2.val:
            list1, list2 = list2, list1

        list1.next = self.mergeTwoLists(list1.next, list2)

        return list1
```

## 복잡도

|            | 시간     | 공간                       |
| ---------- | -------- | -------------------------- |
| Solution 1 | O(n + m) | O(1) — 포인터만 사용       |
| Solution 2 | O(n + m) | O(n + m) — 재귀 호출 스택  |

## 배운 점

- dummy 노드 패턴은 "결과 리스트를 새로 이어 붙일 때" head 처리를 단순화해줌
- 재귀 풀이에서 swap으로 항상 작은 쪽을 list1으로 통일하면 분기를 줄일 수 있음
- Merge Sort의 merge 단계와 동일한 로직
