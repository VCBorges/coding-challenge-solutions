from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        left, right = dummy, head
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next


def compare_binary_trees(
    root1: BinaryTreeNode | None,
    root2: BinaryTreeNode | None,
) -> bool:
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.value != root2.value:
        return False

    return compare_binary_trees(
        root1.left,
        root2.left,
    ) and compare_binary_trees(
        root1.right,
        root2.right,
    )
