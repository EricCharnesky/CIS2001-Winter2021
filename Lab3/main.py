class CircularQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self, initial_size = DEFAULT_CAPACITY):
        self._data = [None] * initial_size
        self._front = 0
        self._back = 0
        self._number_of_items = 0

    def enqueue(self, item):
        self._check_capacity()
        self._data[self._back] = item
        self._back += 1
        if self._back == len(self._data):
            self._back = 0
        self._number_of_items += 1

    def dequeue(self):
        if self._number_of_items == 0:
            raise IndexError
        item = self._data[self._front]
        self._data[self._front] = None
        self._front += 1
        if self._front == len(self._data):
            self._front = 0
        self._number_of_items -= 1
        return item

    def front(self):
        if self._number_of_items == 0:
            raise IndexError
        return self._data[self._front]

    def __len__(self):
        return self._number_of_items

    def _check_capacity(self):
        if self._number_of_items >= len(self._data):
            new_data = [None] * len(self._data) * 2
            new_data_index = 0
            for index in range(self._front, len(self._data)):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1
            for index in range(0, self._back):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1
            self._data = new_data
            self._front = 0
            self._back = self._number_of_items

    def get_raw_contents(self):
        return str(self._data)


queue = CircularQueue()

for number in range(5):
    queue.enqueue(number)

print(queue.get_raw_contents())

queue.dequeue()
queue.dequeue()
queue.dequeue()

print(queue.get_raw_contents())


for number in range(5, 9):
    queue.enqueue(number)

print(queue.get_raw_contents())

queue.dequeue()
queue.dequeue()

print(queue.get_raw_contents())

for number in range(9, 12):
    queue.enqueue(number)

print(queue.get_raw_contents())

for number in range(13, 18):
    queue.enqueue(number)

print(queue.get_raw_contents())