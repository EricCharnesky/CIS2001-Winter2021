# https://github.com/EricCharnesky/CIS2001-Winter2021/blob/5e7bd216e15cc1959dce4860e34e41e8b9d0c876/StacksAndQueues/main.py
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