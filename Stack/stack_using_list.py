class Stack:
    def __init__(self) -> None:
        self.items = list()

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        if not self.is_empty():
            return len(self.items)


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)


print(f"Top element is: {s.peek()}")
print(f"Removed element is: {s.pop()}")
print(f"Top element is: {s.peek()}")
