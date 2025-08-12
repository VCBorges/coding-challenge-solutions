class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtPosition(
    head: SinglyLinkedListNode | None,
    data: int,
    position: int,
) -> SinglyLinkedListNode:
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node

    if position == 0:
        new_node.next = head
        return new_node

    curr_node = head

    for _ in range(position - 1):
        curr_node = curr_node.next

    new_node.next = curr_node.next
    curr_node.next = new_node

    return head
