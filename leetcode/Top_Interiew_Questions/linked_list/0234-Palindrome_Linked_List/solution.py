from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
