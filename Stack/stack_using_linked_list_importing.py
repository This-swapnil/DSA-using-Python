from List.Singly_Linked_List import *


class Stack:
    def __init__(self) -> None:
        self.mylist = singly_link_list()
        self.item_count = 0

    def is_empty(self):
        return self.mylist.is_empty()

    def push(self, data):
        self.mylist.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count -= 1

    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return self.item_count


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
# s.insert(1, 10)

print(f"Total element in Stack: {s.size()}")
print(f"Top element is: {s.peek()}")
print(f"Removed element is: {s.pop()}")
print(f"Top element is: {s.peek()}")
print(f"Total element in Stack: {s.size()}")
