from Item import Item


class TaxableItem(Item):

    def __init__(self, name, price, quantity, tax_rate):
        super().__init__(name, price, quantity)
        self.set_tax_rate(tax_rate)

    def set_tax_rate(self, tax_rate):
        if tax_rate > 1:
            self._tax_rate = tax_rate / 100
        else:
            self._tax_rate = tax_rate

    def get_tax_rate(self):
        return self._tax_rate

    def get_total_price(self):
        return super().get_total_price() * (1 + self._tax_rate)

