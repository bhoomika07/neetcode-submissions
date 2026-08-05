class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.count = 0
        self.head = Node(0)          # front sentinel
        self.tail = Node(0)          # rear sentinel
        self.head.next = self.tail   # empty ring: head -> tail -> head
        self.tail.next = self.head
        self.last = self.head        # last real node; == head when empty

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        new_node.next = self.last.next   # -> tail sentinel
        self.last.next = new_node        # old last -> new node
        self.last = new_node             # new node is now the last real node
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        front = self.head.next
        self.head.next = front.next      # unlink the front node
        if front is self.last:           # removed the only real node
            self.last = self.head
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.data       # front = head.next

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.last.data            # last real node

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity