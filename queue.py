class Queue:

    head = None  # remove from head
    tail = None  # add to tail

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            return 'Empty queue'
        else:
            return self.head.data

    def add(self, val):
        node = Node(val)

        if tail is not None:
            tail.nxt = node
        self.tail = node

        if head is None:
            self.head = node

    def remove(self):
        data = self.head.data
        self.head = self.head.nxt

        if self.head is None:
            self.tail = None

        return data

    class Node:
        data = None
        nxt = None

        def __init__(self, data):
            self.data = data

