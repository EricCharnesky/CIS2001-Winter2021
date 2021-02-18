
class DoublyLinkedList:

    def __init__(self):
        self._head = None  # front
        self._tail = None  # back
        self._number_of_items = 0

    def add_to_front(self, item):
        if self._head is None:
            self._head = self.Node(item)
            self._tail = self._head
        else:
            new_node = self.Node(item, next=self._head)
            self._head.previous = new_node

        self._number_of_items += 1

    def add_to_back(self, item):
        if self._head is None:
            self.add_to_front(item)
        else:
            self._tail.next = self.Node(item, next=None, previous=self._tail)
            self._number_of_items += 1

    def remove_back(self):
        if self._head is None:
            raise ValueError("List is empty")

        data = self._tail.data
        self._tail.data = None

        self._tail = self._tail.previous
        if self._tail is not None:
            self._tail.next = None
        else:
            self._head = None
        self._number_of_items -= 1

        return data

    def remove_front(self):
        if self._head is None:
            raise ValueError("List is empty")

        data = self._head.data
        self._head.data = None

        self._head = self._head.next
        if self._head is not None:
            self._head.previous = None
        else:
            self._tail = None
        self._number_of_items -= 1

        return data

    # O ( k )
    def pop(self, index):
        if not (0 <= index < self._number_of_items):
            raise IndexError("invalid index")

        if index == 0:
            return self.remove_front()
        elif index == self._number_of_items - 1:
            return self.remove_back()
        else:
            current_item = self._head

            for number in range(index):
                current_item = current_item.next

            data = current_item.data
            current_item.data = None

            current_item.previous.next = current_item.next
            current_item.next.previous = current_item.previous

            self._number_of_items -= 1

            # check for new tail
            if current_item.next is None:
                self._tail = current_item

            return data

    class Node:

        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous


class SinglyLinkedList:

    def __init__(self):
        self._head = None  # front
        self._tail = None  # back
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    def add_to_front(self, data):
        new_node = self.Node(data, self._head)
        self._head = new_node

        if self._head.next is None:
            self._tail = new_node

        self._number_of_items += 1

    def add_to_back(self, data):
        new_node = self.Node(data, None)
        if self._tail is None:
            self._tail = new_node
            self._head = new_node
        else:
            self._tail.next = new_node

        self._number_of_items += 1

    def front(self):
        if self._number_of_items == 0:
            raise ValueError("List is empty")

        return self._head.data

    def remove_front(self):
        if self._number_of_items == 0:
            raise ValueError("List is empty")

        data = self._head.data

        self._head.data = None  # cleanup for garbage collection
        self._head = self._head.next

        if self._head is None:
            self._tail = None

        self._number_of_items -= 1

        return data

    # O ( k )
    def get(self, index):
        if not (0 <= index < self._number_of_items):
            raise IndexError("invalid index")
        current_item = self._head

        for number in range(index):
            current_item = current_item.next

        return current_item.data

    # O ( k )
    def pop(self, index):
        if not (0 <= index < self._number_of_items):
            raise IndexError("invalid index")

        if index == 0:
            return self.remove_front()
        else:
            current_item = self._head

            for number in range(index-1):
                current_item = current_item.next

            data = current_item.next.data
            current_item.next.data = None
            current_item.next = current_item.next.next
            self._number_of_items -= 1

            # check for new tail
            if current_item.next is None:
                self._tail = current_item

            return data

    # O ( index ) - no shifting of items after the index
    def add_to_index(self, index, item):
        if not (0 <= index <= self._number_of_items):
            raise IndexError("invalid index")
        if index == 0:
            self.add_to_front(item)
        elif index == self._number_of_items:
            self.add_to_back(item)
        else:
            current_item = self._head

            for number in range(index-1):
                current_item = current_item.next

            new_item = self.Node(item, current_item.next)
            current_item.next = new_item
            self._number_of_items += 1

    # O ( k ) - no shifting of items after the removed item to 'fill' an empty spot
    def remove(self, item):
        if self._number_of_items == 0:
            raise ValueError("List is empty")
        if self._head.data == item:
            self.remove_front()
        else:
            current = self._head
            while current.next is not None:
                if current.next.data == item:
                    # clears the reference for garbage collection
                    current.next.data = None
                    # jump it in the list
                    current.next = current.next.next
                    self._number_of_items -= 1

                    # check for new tail
                    if current.next is None:
                        self._tail = current

                current = current.next
            else:
                raise ValueError("Item not found!")


    class Node:

        def __init__(self, data, next=None):
            self.data = data
            self.next = next


class LLStack:

    def __init__(self):
        self._data = SinglyLinkedList()

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.add_to_front(item)

    def peek(self):
        return self._data.front()

    def pop(self):
        return self._data.remove_front()


class LLQueue:

    def __init__(self):
        self._data = SinglyLinkedList()

    def __len__(self):
        return len(self._data)

    def front(self):
        return self._data.front()

    def enqueue(self, data):
        self._data.add_to_back(data)

    def dequeue(self):
        return self._data.remove_front()


some_list = SinglyLinkedList()

for n in range(10):
    some_list.add_to_front(n)

some_list.add_to_index(5, 100)

for n in range(len(some_list)):
    print(some_list.get(n))

some_list.pop(5)

for n in range(len(some_list)):
    print(some_list.get(n))