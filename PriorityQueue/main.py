class PriorityQueue:

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

    def add(self, key, value=None):
        self._number_of_items += 1

    def remove_min(self):
        pass

    def min(self):
        return self._data[0]

    def __len__(self):
        return self._number_of_items

    def is_empty(self):
        return len(self) == 0