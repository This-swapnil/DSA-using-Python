class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next


class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def enqueue(self, data):
        n = Node(item=data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.item_count == 1:  # self.front==self.rear
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return self.item_count


# driver code
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print(f"Front value: {q.get_front()}")
print(f"Rear value: {q.get_rear()}")
print(f"Queue has {q.size()} element(s)")

q.dequeue()

print(f"Front value: {q.get_front()}")
print(f"Rear value: {q.get_rear()}")
print(f"Queue has {q.size()} element(s)")
