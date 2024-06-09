class SinglyLinkedListNode:
    def __init__(self, node_data: int):
        self.data = node_data
        self.next: SinglyLinkedListNode | None = None


class SinglyLinkedList:
    def __init__(self):
        self.head: SinglyLinkedListNode | None = None
        self.tail: SinglyLinkedListNode | None = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def printLinkedList(head: SinglyLinkedListNode) -> None:
    current_node = head
    data = []
    while current_node:
        data.append(current_node.data)
        current_node = current_node.next

    print('\n'.join(list(map(str, data))))


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)