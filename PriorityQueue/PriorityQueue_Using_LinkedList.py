class Node:
    def __init__(self, items=None, priority=None, next=None) -> None:
        self.item = items
        self.priority = priority
        self.next = next


class PriorityQueue:
    def __init__(self) -> None:
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None

    def push(self, data, priority):
        n = Node(items=data, priority=priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            current = self.start
            while current.next and current.next.priority <= priority:
                current = current.next
            n.next = current.next
            current.next = n
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("Priority Queue is empty")

    def size(self):
        return self.item_count


pq = PriorityQueue()
pq.push("swapnil", 7)
pq.push("kunal", 2)
pq.push("ganesh", 4)
pq.push("samir", 3)
pq.push("akshay", 6)
pq.push("karan", 5)
pq.push("prasad", 1)

print(f"Size of Priority Queue before deletion is: {pq.size()}")

while not pq.is_empty():
    print(pq.pop())
