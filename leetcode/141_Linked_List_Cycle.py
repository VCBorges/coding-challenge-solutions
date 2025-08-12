from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle_tortoise_and_hare(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        hash = {}
        hash[head] = True
        while curr:
            if curr.next is None:
                return False

            curr = curr.next
            if curr in hash:
                return True

            hash[curr] = True
