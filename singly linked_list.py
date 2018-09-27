class Node:

    value = None
    nxt = None

    def __init__(self, val):
        self.value = val
        self.nxt = None


def create_linked_list(arr):
    node = Node(arr[0])

    for i in range(1, len(arr)):
        n = Node(arr[1])
        node.set_next(n)
        node = n


if __name__ == '__main__':
    nos = int(raw_input())

    arr = []

    for i in range(0, nos):
        arr.append(raw_input())

    print arr
