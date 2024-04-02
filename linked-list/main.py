class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# This Python class defines a linked list data structure with methods to initialize the list and print its elements.
class LinkedList:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None


my_linked_list = LinkedList(4)

my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.pop(8)
print(my_linked_list.n.value)
