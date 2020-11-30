class Node:
    def __init__(self, next_node=None, value=None):
        self.value = value
        self.next = next_node


class SinglyLinkedList:
    def __init__(self, head):
        self.head = head

    def push(self, push_after_node=None, value=None):
        if not push_after_node:
            push_after_node = self.tail

        new_node = Node(next_node=push_after_node.next, value=value)

        push_after_node.next = new_node

        return

    def pop(self, delete_node=None):
        if not delete_node:
            delete_node = self.tail

        current_node = self.head

        while current_node.next != delete_node:
            current_node = current_node.next

        if delete_node.next:
            current_node.next = delete_node.next
        else:
            current_node.next = None

        del delete_node

        return

    @property
    def tail(self):
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        return current_node

    def traverse(self, node=None):
        if not node:
            node = self.head

        while node:
            print(node.value)

            node = node.next

        return

