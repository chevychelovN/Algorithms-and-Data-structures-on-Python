from collections import deque


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


pq = Queue()
pq.enqueue(1)
pq.enqueue(2)
pq.enqueue(3)
print(pq.buffer)
pq.dequeue()
print(pq.buffer)
