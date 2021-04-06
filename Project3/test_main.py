from unittest import TestCase
from Polynomial import Polynomial


class TestPolynomial(TestCase):

    def test_string(self):
        # arrange
        expected_string = "3.00x^7"

        # act
        poly = Polynomial(3, 7)
        actual_string = str(poly)

        # assert
        self.assertEqual(expected_string, actual_string)

    def test_string_negative(self):
        # arrange
        expected_string = "-3.00x^7"

        # act
        poly = Polynomial(-3, 7)
        actual_string = str(poly)

        # assert
        self.assertEqual(expected_string, actual_string)

    def test_string_negative_plus_negative(self):
        # arrange
        expected_string = "-3.00x^7 -2.00x^5"

        # act
        poly = Polynomial(-3, 7) + Polynomial(-2, 5)

        actual_string = str(poly)

        # assert
        self.assertEqual(expected_string, actual_string)

    def test_add_monomials(self):
        # arrange
        expected_string = "3.00x^7 + 5.00x^3"
        poly1 = Polynomial(3, 7)
        poly2 = Polynomial(5, 3)

        # act
        poly3 = poly1 + poly2
        actual_string1 = str(poly3)
        poly4 = poly2 + poly1
        actual_string2 = str(poly4)

        # assert
        self.assertEqual(expected_string, actual_string1)
        self.assertEqual(expected_string, actual_string2)

    def test_add_monomials_duplicate_exponents(self):
        # arrange
        expected_string = "3.00x^7 + 8.00x^3"
        poly1 = Polynomial(3, 7)
        poly2 = Polynomial(5, 3)
        poly3 = poly1 + poly2
        poly4 = Polynomial(3, 3)

        # act
        poly5 = poly3 + poly4
        actual_string1 = str(poly5)
        poly6 = poly4 + poly3
        actual_string2 = str(poly6)

        # assert
        self.assertEqual(expected_string, actual_string1)
        self.assertEqual(expected_string, actual_string2)

    def test_add_polynomialss(self):
        # arrange
        expected_string = "3.00x^7 + 5.00x^6 + 2.00x^5 + 3.00x^4 + 5.00x^3"
        poly1 = Polynomial(3, 7)
        poly2 = Polynomial(5, 3)
        poly3 = poly1 + poly2
        poly4 = Polynomial(5, 6)
        poly5 = Polynomial(2, 5)
        poly6 = poly4 + poly5
        poly7 = poly6 + Polynomial(3, 4)
        poly8 = poly7 + poly3

        # act
        actual_string = str(poly8)

        # assert
        self.assertEqual(expected_string, actual_string)

    def test_multiply_monomials(self):
        # arrange
        expected_string = "6.00x^7"
        poly1 = Polynomial(2, 3)
        poly2 = Polynomial(3, 4)

        # act
        poly3 = poly1 * poly2
        poly4 = poly2 * poly1
        actual_string1 = str(poly3)
        actual_string2 = str(poly4)


        # assert
        self.assertEqual(expected_string, actual_string1)
        self.assertEqual(expected_string, actual_string2)

    def test_multiply_polynomials(self):
        # arrange
        expected_string = "12.00x^13 + 9.00x^10 + 20.00x^9 + 15.00x^6"
        poly1 = Polynomial(3, 7) + Polynomial(5, 3)
        poly2 = Polynomial(4, 6) + Polynomial(3, 3)

        # act
        poly5 = poly1 * poly2
        actual_string1 = str(poly5)
        poly6 = poly2 * poly1
        actual_string2 = str(poly6)

        # assert
        self.assertEqual(expected_string, actual_string1)
        self.assertEqual(expected_string, actual_string2)

    def test_equals(self):
        poly1 = Polynomial(3, 4) + Polynomial(4, 5)
        poly2 = Polynomial(4, 5) + Polynomial(3, 4)

        self.assertTrue(poly1 == poly2)
        self.assertFalse(poly1 != poly2)

    def test_equals_different_length(self):
        poly1 = Polynomial(3, 4) + Polynomial(4, 5)
        poly2 = Polynomial(4, 5) + Polynomial(3, 4) + Polynomial(2, 2)

        self.assertTrue(poly1 != poly2)
        self.assertFalse(poly1 == poly2)

    def test_differentiate(self):
        expected_original = "4.00x^5 + 3.00x^4"
        expected_string = "20.00x^4 + 12.00x^3"
        poly1 = Polynomial(3, 4) + Polynomial(4, 5)

        poly2 = poly1.differentiate()
        actual_string = str(poly2)
        actual_original_string = str(poly1)

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(expected_original, actual_original_string)

    def test_integration(self):
        expected_original = "4.00x^5 + 3.00x^4"
        expected_string = "20.00x^4 + 12.00x^3"
        poly1 = Polynomial(3, 4) + Polynomial(4, 5)

        poly2 = poly1.differentiate()
        actual_string = str(poly2)
        actual_original_string = str(poly1)
        poly3 = poly2.integrate()
        integrted_string = str(poly3)

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(expected_original, actual_original_string)
        self.assertEqual(expected_original, integrted_string)

    def test_zero_exponent_string(self):
        expected_string = "3.00"

        poly1 = Polynomial(3, 0)

        actual_string = str(poly1)

        self.assertEqual(expected_string, actual_string)


