class Stack(list):  # defining class stack by inheriting(extending) list class
    def is_empty(self):
        return (
            len(self) == 0
        )  # here self is refer to parent class i.e list as well as Stack class

    def push(self, data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self)

    def insert(self, index, data):
        raise AttributeError("No attribute 'insert' in Stack")


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
# s.insert(1, 10)


print(f"Top element is: {s.peek()}")
print(f"Removed element is: {s.pop()}")
print(f"Top element is: {s.peek()}")
