# mostly sourced from the book

class DynamicArray:

    def __init__(self):
        self._number_of_items = 0
        self._data = [None]

    def __len__(self):
        return self._number_of_items

    def __getitem__(self, index):
        self.is_valid_index(index)
        return self._data[index]

    def is_valid_index(self, index):
        if not 0 <= index < self._number_of_items:
            raise IndexError

    def append(self, item):
        self._check_and_resize()
        self._data[self._number_of_items] = item
        self._number_of_items += 1

    def index(self, item):
        for index in range(self._number_of_items):
            if self._data[index] == item:
                return index
        raise ValueError(f'{item} not in dynamicarray')

    def count(self, item):
        occurrences = 0
        for index in range(self._number_of_items):
            if self._data[index] == item:
                occurrences += 1
        return occurrences

    def insert(self, index, item):
        self.is_valid_index(index)
        self._check_and_resize()
        for index in range(self._number_of_items, index, -1):
            self._data[index] = self._data[index-1]
        self._data[index] = item
        self._number_of_items += 1

    def remove(self, item):
        for index in range(self._number_of_items):
            if self._data[index] == item:
                for index_to_replace in range(index, self._number_of_items):
                    self._data[index_to_replace] = self._data[index_to_replace+1]
                self._number_of_items -= 1
                self._data[self._number_of_items] = None
                return
        raise ValueError('value not found')

    def _check_and_resize(self):
        if self._number_of_items == len(self._data):
            new_data = [None] * len(self._data) * 2
            for index in range(len(self._data)):
                new_data[index] = self._data[index]
            self._data = new_data


some_list = []

index = some_list.index(10)

test_array = DynamicArray()

for number in range(10):
    test_array.append(number)

for index in range(len(test_array)):
    print(test_array[index])
