from unittest import TestCase
from TaxableItem import TaxableItem

class TestTaxableItem(TestCase):
    def test_set_tax_rate(self):
        # arrange
        expected_tax_rate = .06

        # act
        table = TaxableItem("table", 2, 1, 0)
        table.set_tax_rate(.06)
        actual_tax_rate = table.get_tax_rate()

        # assert
        self.assertEqual(expected_tax_rate, actual_tax_rate)

    def test_set_tax_rate_whole_number(self):
        # arrange
        expected_tax_rate = .06

        # act
        table = TaxableItem("table", 2, 1, 0)
        table.set_tax_rate(6)
        actual_tax_rate = table.get_tax_rate()

        # assert
        self.assertEqual(expected_tax_rate, actual_tax_rate)


    def test_get_total_price(self):
        # arrange
        expected_total_price = 4 * 1.06

        # act
        table = TaxableItem("table", 2, 2, 6)
        actual_total_price = table.get_total_price()

        # assert
        self.assertEqual(expected_total_price, actual_total_price)
