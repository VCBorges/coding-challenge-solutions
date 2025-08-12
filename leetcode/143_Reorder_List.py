from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)
        for i in range(n // 2):
            nodes[i].next = nodes[n - i - 1]
            if i + 1 < n - i - 1:
                nodes[n - i - 1].next = nodes[i + 1]

        nodes[n // 2].next = None
