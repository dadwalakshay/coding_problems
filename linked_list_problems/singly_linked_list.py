from base import BaseLinkedList


class Node:
    def __init__(self, _next=None, value=None):
        self.next = _next
        self.value = value
    
    def __str__(self):
        return f'{self.value}'


class SinglyLinkedList(BaseLinkedList):
    def __init__(self, value=None):
        self.head = Node(value=value)
    
    def __iter__(self):
        self.next_node = self.head

        return self
    
    def __next__(self):
        current_node = self.next_node

        if not current_node:
            raise StopIteration

        self.next_node = current_node.next

        return current_node
    
    def insert(self, node=None, value=None):
        if not node:
            # If Node's location not available, it'll insert new Node at the
            # end of LinkedList.
            node = self.tail

        new_node = Node(_next=node.next, value=value)

        node.next = new_node

        return
    
    def update(self, node=None, value=None):
        # Updates value of given Node with updated value.
        if not node:
            raise ValueError("Node to be updated can not be None.")

        node.value = value

        return

    def delete(self, node=None):
        # Deletes Last Node if not given.
        if not node:
            node = self.tail

        current_node = self.head

        while current_node.next != node:
            current_node = current_node.next

        if node.next:
            current_node.next = node.next
        else:
            current_node.next = None

        del node

        return

    @property
    def tail(self):
        # Traverses the LinkedList and returns tail Node.
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        return current_node
