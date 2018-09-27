class Stack:

    top = None  # add and remove form here

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            return 'Empty stack'
        else:
            return self.top.data

    def push(self, data):
        node = Node(data)
        node.nxt = self.top
        self.top = node

    def pop(self):
        if self.top is not None:
            data = self.top.data
            self.top = self.top.nxt
            return data
        else:
            return 'Empty stack'

    class Node:
        data = None
        nxt = None

        def __init__(self, data):
            self.data = data
