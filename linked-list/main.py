class Node:
    def __init__(self, value):
        self.value = value
        self.node = None


class LinkedList:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 1


my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
