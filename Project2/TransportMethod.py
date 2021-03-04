class TransportMethod:

    def __init__(self, number, number_of_items_until_full, load_time_multiple=1):
        self.number = number
        self.number_of_items_until_full = number_of_items_until_full
        self.time_until_full = 0
        self.current_number_of_items = 0
        self.load_time_multiple = load_time_multiple

    def load_item(self, current_time_elapsed):
        self.current_number_of_items += 1
        current_time_elapsed += self.number * self.load_time_multiple
        if self.current_number_of_items == self.number_of_items_until_full:
            self.time_until_full = current_time_elapsed
        return current_time_elapsed + self.number * self.load_time_multiple

