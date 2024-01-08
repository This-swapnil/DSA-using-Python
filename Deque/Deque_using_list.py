from requests import delete


class Deque:
    def __init__(self) -> None:
        self.items = list()

    def is_empty(self):
        return len(self.items) == 0

    def insert_front(self, data):
        self.items.insert(0, data)

    def insert_rear(self, data):
        self.items.append(data)

    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Deque is empty")

    def delete_rear(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("Deque is empty")

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Deque is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Deque is empty")

    def size(self):
        return len(self.items)


q = Deque()
q.insert_front(10)
q.insert_front(20)
q.insert_rear(30)
q.insert_rear(40)

print(f"Front value: {q.get_front()}")
print(f"Rear value: {q.get_rear()}")
print(f"Queue has {q.size()} element(s)")

q.delete_front()

print(f"Front value after delete front: {q.get_front()}")
print(f"Rear value after delete front: {q.get_rear()}")
print(f"Queue has {q.size()} element(s)")

q.delete_rear()

print(f"Front value after delete rear: {q.get_front()}")
print(f"Rear value after delete rear: {q.get_rear()}")
print(f"Queue has {q.size()} element(s)")
