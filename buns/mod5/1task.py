class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node.value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def display(self):
        current = self.head
        stack = []
        while current:
            stack.append(current.value)
            current = current.next
        return stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.display())  
print(stack.peek())
stack.pop()
print(stack.display())
print(stack.peek())
stack.pop()
print(stack.display())

