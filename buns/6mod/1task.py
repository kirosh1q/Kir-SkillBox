class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
 
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next
        return curr_node.data
 
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            removed_node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            prev_node = None
            curr_node = self.head
            for _ in range(index):
                prev_node = curr_node
                curr_node = curr_node.next
            removed_node = curr_node
            prev_node.next = curr_node.next
            if curr_node == self.tail:
                self.tail = prev_node
        self.size -= 1
        return removed_node.data
 
    def insert(self, n, val):
        if n < 0 or n > self.size:
            raise IndexError("Index out of range")
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            prev_node = None
            curr_node = self.head
            for _ in range(n):
                prev_node = curr_node
                curr_node = curr_node.next
            new_node.next = curr_node
            prev_node.next = new_node
            if curr_node is None:
                self.tail = new_node
        self.size += 1
 
    def __iter__(self):
        curr_node = self.head
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.next

linked_list = LinkedList()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.push(4)

for data in linked_list:
    print(data)
    print(linked_list.get(2))
    linked_list.insert(2, 10)
for data in linked_list:
    print(data)
    linked_list.remove(1)
for data in linked_list:
    print(data)