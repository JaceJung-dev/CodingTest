# 234. Palindrome Linked List

## 문제

- 링크: https://leetcode.com/problems/palindrome-linked-list/
- 난이도: Easy
- 태그: Linked List, Two Pointers, Stack, Recursion

## 접근 방식

### Solution 1 — 배열 변환 + Two Pointers

- 리스트를 배열로 변환 후 양 끝에서 비교

### Solution 2 — Fast/Slow로 중간 찾기 + 뒤집기

- fast/slow로 중간 지점을 찾고
- 뒤쪽 절반을 reverse한 뒤 앞쪽과 비교

### Solution 3 — Stack

- 전체 값을 스택에 push 후
- 다시 순회하며 pop한 값(역순)과 비교

## 풀이

### Solution 1

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next

        left, right = 0, len(node_list) - 1
        while left < right:
            if node_list[left] != node_list[right]:
                return False

            left += 1
            right -= 1

        return True
```

### Solution 2

```python
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # 중간 찾기
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 뒤쪽 절반 뒤집기
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 앞 절반 뒤 절반 비교
        front = head
        back = prev

        while back:
            if front.val != back.val:
                return False
            front = front.next
            back = back.next

        return True
```

### Solution 3

```python
class Solution3:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head

        while curr and curr.val == stack.pop():
            curr = curr.next

        return curr is None
```

## 복잡도

|            | 시간 | 공간                    |
| ---------- | ---- | ----------------------- |
| Solution 1 | O(n) | O(n) — 배열 저장        |
| Solution 2 | O(n) | O(1) — in-place reverse |
| Solution 3 | O(n) | O(n) — 스택 저장        |

## 배운 점

- Solution 2가 공간 O(1)로 가장 효율적 — fast/slow + reverse + 비교 세 기법의 조합
- 스택의 LIFO 특성을 활용하면 역순 비교를 자연스럽게 구현 가능
- 링크드 리스트는 인덱스 접근이 안 되므로, 팰린드롬 판별에 배열 변환이나 reverse 같은 전처리가 필요
