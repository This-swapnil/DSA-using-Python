class PriorityQueue:
    def __init__(self) -> None:
        self.items = list()

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data, priority):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index, (data, priority))

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)[0]
        else:
            raise IndexError("Priority Queue is empty")

    def size(self):
        return len(self.items)


# driver code
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
