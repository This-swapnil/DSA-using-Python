from turtle import left, right


class Heap:
    def __init__(self) -> None:
        self.heap = list()

    def create_heap(self, list):
        for i in list:
            self.insert(i)

    def insert(self, item):
        index = len(self.heap)
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[parent_index] < item:
            if index == len(self.heap):
                self.heap.append(self.heap[parent_index])
            else:
                self.heap[index] = self.heap[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2
        if index == len(self.heap):
            self.heap.append(item)
        else:
            self.heap[index] = item

    def top_element(self):
        if not len(self.heap) == 0:
            return self.heap[0]
        else:
            raise EmptyHeapException

    def delete(self):
        if not len(self.heap) == 0:
            if len(self.heap) == 1:
                return self.heap.pop()
            max_value = self.heap[0]
            temp = self.heap.pop()
            index = 0
            leftChildIndex = 2 * index + 1
            rihgtChildIndex = 2 * index + 2

            while leftChildIndex < len(self.heap):
                if rihgtChildIndex < len(self.heap):
                    if self.heap[leftChildIndex] > self.heap[rihgtChildIndex]:
                        if self.heap[leftChildIndex] > temp:
                            self.heap[index] = self.heap[leftChildIndex]
                            index = leftChildIndex
                        else:
                            break
                    else:
                        if self.heap[rihgtChildIndex] > temp:
                            self.heap[index] = self.heap[rihgtChildIndex]
                            index = rihgtChildIndex
                        else:
                            break
                else:  # no right child
                    if self.heap[leftChildIndex] > temp:
                        self.heap[index] = self.heap[leftChildIndex]
                        index = leftChildIndex
                    else:
                        break
                leftChildIndex = 2 * index + 1
                rihgtChildIndex = 2 * index + 2
            self.heap[index] = temp
            return max_value
        else:
            raise EmptyHeapException

    def heapSort(self, lst):
        self.create_heap(lst)
        lst2 = list()
        try:
            while True:
                lst2.insert(0, self.delete())
        except EmptyHeapException:
            pass
        return lst2


class EmptyHeapException(Exception):
    def __init__(self, msg="Heap is empty"):
        self.msg = msg

    def __str__(self):
        return self.msg


lst = [34, 56, 12, 78, 43, 25, 10, 80, 60]
h = Heap()
lst = h.heapSort(lst)
print(lst)
