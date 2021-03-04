from Stack import Stack
from Queue import Queue
from TransportMethod import TransportMethod


class Dock:

    MAX_STACK_SIZE = 5
    PLANE_LOAD_ONE_WAY_TIME = 5

    def __init__(self, number_of_items_per_train_list, number_of_items_per_plane_list,
                 train_item_list, plane_item_list):
        self._trains = []
        for index in range(len(number_of_items_per_train_list)):
            self._trains.append(TransportMethod(index + 1, number_of_items_per_train_list[index]))

        self._planes = []
        for index in range(len(number_of_items_per_plane_list)):
            self._planes.append(TransportMethod(index + 1, number_of_items_per_plane_list[index], self.PLANE_LOAD_ONE_WAY_TIME))

        self._train_items = Queue()
        self._plane_items = Queue()

        self._unload_train_items_from_ship(train_item_list)
        self._unload_plane_items_from_ship(plane_item_list)

        self._load_items_on_trains()

        self._load_items_on_planes()

    def _unload_train_items_from_ship(self, train_item_list):
        stack = Stack()
        for item in train_item_list:
            stack.push(item)
            if len(stack) == self.MAX_STACK_SIZE:
                self._train_items.enqueue(stack)
                stack = Stack()
        if len(stack) > 0:
            self._train_items.enqueue(stack)

    def _unload_plane_items_from_ship(self, plane_item_list):
        for item in plane_item_list:
            self._plane_items.enqueue(item)

    def _load_items_on_trains(self):
        current_time = 0
        while len(self._train_items) > 0:
            stack = self._train_items.dequeue()
            while len(stack) > 0:
                item = stack.pop()
                current_time = self._trains[item - 1].load_item(current_time)

    def _load_items_on_planes(self):
        current_time = 0
        while len(self._plane_items) > 0:
            item = self._plane_items.dequeue()
            current_time = self._planes[item - 1].load_item(current_time)

    def get_train_load_times(self):

        return " ".join(str(train.time_until_full) for train in self._trains)

    def get_plane_load_times(self):

        return " ".join(str(plane.time_until_full) for plane in self._planes)





