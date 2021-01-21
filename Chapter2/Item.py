class Item:

    def __init__(self, name, price, quantity):
        self._name = name
        self.set_price(price)
        self.set_quantity(quantity)

    def set_price(self, price):
        if price < 0:
            raise ValueError('Price may not be < 0')
        self._price = price

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError('Quantity may not be < 0')
        self._quantity = quantity

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    def get_total_price(self):
        return self._quantity * self._price

