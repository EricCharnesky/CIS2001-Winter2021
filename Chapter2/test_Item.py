from unittest import TestCase
from Item import Item

class TestItem(TestCase):
    def test_set_price(self):
        # Arrange
        expected_price = 2.5
        nacho = Item("nacho", 0, 1)

        # Act
        nacho.set_price(expected_price)
        actual_price = nacho.get_price()

        # Assert
        self.assertEqual(expected_price, actual_price)

    def test_set_price_raises_error(self):
        # Arrange
        nacho = Item("nacho", 0, 1)
        invalid_price = -1
        # Act

        # Assert
        self.assertRaises(ValueError, nacho.set_price, invalid_price)

    def test_set_quantity(self):
        # Arrange
        expected_quantity = 42
        nacho = Item("nacho", 0, 0)

        # Act
        nacho.set_quantity(expected_quantity)
        actual_quantity = nacho.get_quantity()

        # Assert
        self.assertEqual(expected_quantity, actual_quantity)

    def test_set_quantity_raises_error(self):
        # Arrange
        nacho = Item("nacho", 0, 1)
        invalid_quantity = -1

        # Act

        # Assert
        self.assertRaises(ValueError, nacho.set_quantity, invalid_quantity)

    def test_get_name(self):
        # Arrange
        expected_name = "nacho"

        # Act
        nacho = Item(expected_name, 0, 0)
        actual_name = nacho.get_name()

        # Assert
        self.assertEqual(expected_name, actual_name)

    def test_get_total_price(self):
        # Arrange
        price = 2.5
        quantity = 42
        expected_total_price = price * quantity

        # Act
        nacho = Item("nacho", price, quantity)
        actual_total_price = nacho.get_total_price()

        # Assert
        self.assertEqual(expected_total_price, actual_total_price)
