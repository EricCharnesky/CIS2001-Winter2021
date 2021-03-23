import random


class MinimumPriorityQueue:

    # use binary tree structure in array based storage

    class _Item:

        def __init__(self, key, value):
            self._key = key
            self._value = value

        # only need less than because we are a min queue
        def __lt__(self, other):
            return self._key < other._key

    def __init__(self):
        self._data = [None]
        self._number_of_items = 0

    # O(log n)
    def add(self, key, value=None):
        if self._number_of_items == len(self._data):
            self._increase_size()

        item = self._Item(key, value)
        self._data[self._number_of_items] = item
        self._upheap(self._number_of_items)

        self._number_of_items += 1

    def _increase_size(self):
        new_data = [None] * len(self._data) * 2
        for index in range(len(self._data)):
            new_data[index] = self._data[index]
        self._data = new_data

    def _upheap(self, index):
        # stops when index is the top of the heap
        if index != 0:
            parent_index = self._parent(index)

            if self._data[index] < self._data[parent_index]:
                self._swap(index, parent_index)
                self._upheap(parent_index)

    def _swap(self, index, new_index):
        temp = self._data[index]
        self._data[index] = self._data[new_index]
        self._data[new_index] = temp

        # one liner, because python is awesome
        # self._data[index], self._data[new_index] = self._data[new_index], self._data[index]

    def _downheap(self, index):
        smallest_child_index = None
        if self._is_valid_index(self._right_child(index)):
            smallest_child_index = self._right_child(index)
            if self._data[self._left_child(index)] < self._data[smallest_child_index]:
                smallest_child_index = self._left_child(index)
        elif self._is_valid_index(self._left_child(index)):
            smallest_child_index = self._left_child(index)

        if smallest_child_index is not None:
            if self._data[smallest_child_index] < self._data[index]:
                self._swap(smallest_child_index, index)
                self._downheap(smallest_child_index)

    # O(log n)
    def remove_min(self):
        self._number_of_items -= 1
        self._swap(0, self._number_of_items)
        item = self._data[self._number_of_items]
        self._data[self._number_of_items] = None
        self._downheap(0)
        return item._key, item._value

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def _is_valid_index(self, index):
        return index < self._number_of_items and index >= 0

    # O(1)
    def min(self):
        return self._data[0]._key, self._data[0]._value

    def __len__(self):
        return self._number_of_items

    def is_empty(self):
        return len(self) == 0

class MaximumPriorityQueue:

    # use binary tree structure in array based storage

    class _Item:

        def __init__(self, key, value):
            self._key = key
            self._value = value

        # only need less than because we are a min queue
        def __gt__(self, other):
            return self._key > other._key

    def __init__(self):
        self._data = [None]
        self._number_of_items = 0

    # O(log n)
    def add(self, key, value=None):
        if self._number_of_items == len(self._data):
            self._increase_size()

        item = self._Item(key, value)
        self._data[self._number_of_items] = item
        self._upheap(self._number_of_items)

        self._number_of_items += 1

    def _increase_size(self):
        new_data = [None] * len(self._data) * 2
        for index in range(len(self._data)):
            new_data[index] = self._data[index]
        self._data = new_data

    def _upheap(self, index):
        # stops when index is the top of the heap
        if index != 0:
            parent_index = self._parent(index)

            if self._data[index] > self._data[parent_index]:
                self._swap(index, parent_index)
                self._upheap(parent_index)

    def _swap(self, index, new_index):
        temp = self._data[index]
        self._data[index] = self._data[new_index]
        self._data[new_index] = temp

        # one liner, because python is awesome
        # self._data[index], self._data[new_index] = self._data[new_index], self._data[index]

    def _downheap(self, index):
        largest_child_index = None
        if self._is_valid_index(self._right_child(index)):
            largest_child_index = self._right_child(index)
            if self._data[self._left_child(index)] > self._data[largest_child_index]:
                largest_child_index = self._left_child(index)
        elif self._is_valid_index(self._left_child(index)):
            largest_child_index = self._left_child(index)

        if largest_child_index is not None:
            if self._data[largest_child_index] > self._data[index]:
                self._swap(largest_child_index, index)
                self._downheap(largest_child_index)

    # O(log n)
    def remove_max(self):
        self._number_of_items -= 1
        self._swap(0, self._number_of_items)
        item = self._data[self._number_of_items]
        self._data[self._number_of_items] = None
        self._downheap(0)
        return item._key, item._value

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def _is_valid_index(self, index):
        return index < self._number_of_items and index >= 0

    # O(1)
    def max(self):
        return self._data[0]._key, self._data[0]._value

    def __len__(self):
        return self._number_of_items

    def is_empty(self):
        return len(self) == 0


priority_queue = MinimumPriorityQueue()

for number in range(20):
    priority_queue.add(random.randint(0,100))

while not priority_queue.is_empty():
    print(priority_queue.remove_min())

max_priority_queue = MaximumPriorityQueue()

for number in range(20):
    max_priority_queue.add(random.randint(0, 100))

while not max_priority_queue.is_empty():
    print(max_priority_queue.remove_max())

