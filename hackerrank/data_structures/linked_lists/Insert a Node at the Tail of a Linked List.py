class SinglyLinkedListNode:
    def __init__(self, node_data: int):
        self.data = node_data
        self.next: SinglyLinkedListNode = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtTail(
    head: SinglyLinkedListNode | None,
    data: int,
) -> SinglyLinkedListNode:
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node

    current_node = head
    while current_node.next:
        current_node = current_node.next
    current_node.next = new_node
    return head


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head
