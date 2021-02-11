# stack - First In Last Out - FILO - LIFO
# queue - First in First Out - FIFO


class DumbQueue:

    def __init__(self):
        self._data = []

    # O(1)
    def enqueue(self, item):
        self._data.append(item)

    # O(n) - this is a problem
    def dequeue(self):
        if len(self._data) == 0:
            raise ValueError("Queue is empty")
        return self._data.pop(0)

    # O(1)
    def front(self):
        if len(self._data) == 0:
            raise ValueError("Queue is empty")
        return self._data[0]


# faster, but never resizes the internal list storage - uses too much memory
class FasterDumbQueue:

    def __init__(self):
        self._data = []
        self._front_index = 0

    def __len__(self):
        return len(self._data) - self._front_index

    # O(1)
    def enqueue(self, item):
        self._data.append(item)

    # O(1)
    def dequeue(self):
        if len(self._data) == 0 or self._front_index == len(self._data):
            raise ValueError("Queue is empty")
        item = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index += 1
        return item

    # O(1)
    def front(self):
        if len(self._data) == 0 or self._front_index == len(self._data):
            raise ValueError("Queue is empty")
        return self._data[self._front_index]


# wrapper around list to prevent other access
class Stack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    # O(1)
    def push(self, item):
        self._data.append(item)

    # O(1)
    def peek(self):
        if len(self._data) == 0:
            raise ValueError("Stack is empty")
        return self._data[len(self._data) - 1]

    # O(1)
    def pop(self):
        if len(self._data) == 0:
            raise ValueError("Stack is empty")
        return self._data.pop(len(self._data) - 1)



my_stack = Stack()

for number in range(10):
    my_stack.push(number)

while len(my_stack) > 0:
    print(my_stack.pop())


my_list = []

for number in range(10):
    my_list.append(number)

my_list.insert(0, 42)

while len(my_list) > 0:
    print(my_list.pop())



my_queue = FasterDumbQueue()

for number in range(10):
    my_queue.enqueue(number)

while len(my_queue) > 0:
    print(my_queue.dequeue())

