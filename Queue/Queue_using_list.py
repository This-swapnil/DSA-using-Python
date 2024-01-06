class Queue:
    def __init__(self) -> None:
        self.items = list()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(f"Front value: {q.get_front()}")
print(f"Rear value: {q.get_rear()}")
print(f"Queue has {q.size()} element(s)")

q.dequeue()

print(f"Front value: {q.get_front()}")
print(f"Rear value: {q.get_rear()}")
print(f"Queue has {q.size()} element(s)")
