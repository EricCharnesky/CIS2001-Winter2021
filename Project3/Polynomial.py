class Polynomial:

    class TermNode:

        def __init__(self, coefficient, exponent, next=None):
            self.coefficient = coefficient
            self.exponent = exponent
            self.next = next

        def __eq__(self, other):
            return type(other) is type(self) \
                    and self.coefficient == other.coefficient \
                    and self.exponent == other.exponent

        def __ne__(self, other):
            return not(self == other)

    def __init__(self, coefficient, exponent):
        self._first_node = self.TermNode(coefficient, exponent)

    def __add__(self, other):
        new_poly = Polynomial(self._first_node.coefficient, self._first_node.exponent)

        current_term = self._first_node.next
        other_current_term = other._first_node

        while current_term is not None:
            new_poly._addTermInDescendingOrder(current_term)
            current_term = current_term.next

        while other_current_term is not None:
            new_poly._addTermInDescendingOrder(other_current_term)
            other_current_term = other_current_term.next

        return new_poly

    def __mul__(self, other):
        new_poly = None

        current_term = self._first_node
        while current_term is not None:

            other_current_term = other._first_node
            while other_current_term is not None:

                if new_poly is None:
                    new_poly = Polynomial(current_term.coefficient * other_current_term.coefficient,
                                current_term.exponent + other_current_term.exponent)
                else:
                    new_poly._addTermInDescendingOrder(
                        self.TermNode(current_term.coefficient * other_current_term.coefficient,
                        current_term.exponent + other_current_term.exponent))

                other_current_term = other_current_term.next
            current_term = current_term.next

        return new_poly

    def _addTermInDescendingOrder(self, term):
        term = self.TermNode(term.coefficient, term.exponent)
        if term.exponent > self._first_node.exponent:
            term.next = self._first_node
            self._first_node = term
        elif term.exponent == self._first_node.exponent:
            self._first_node.coefficient += term.coefficient
        else:
            current_term = self._first_node
            while current_term.next is not None and term.exponent <= current_term.next.exponent:
                if term.exponent < current_term.next.exponent:
                    current_term = current_term.next
                else:
                    current_term.next.coefficient += term.coefficient
                    return

            term.next = current_term.next
            current_term.next = term

    def __str__(self):
        result = ""
        current_term = self._first_node
        while current_term is not None:
            if current_term.coefficient < 0 and len(result) > 2:
                result = result[:-2]

            if current_term.coefficient != 0:
                if current_term.exponent != 0:
                    result += f"{current_term.coefficient:.02f}x^{current_term.exponent} + "
                else:
                    result += f"{current_term.coefficient:.02f} + "
            current_term = current_term.next
        return result[:-3]

    def __eq__(self, other):
        if type(other) is not type(self):
            return False
        current_term = self._first_node
        other_current_term = other._first_node

        while current_term is not None and other_current_term is not None:
            if current_term != other_current_term:
                return False
            current_term = current_term.next
            other_current_term = other_current_term.next

        return current_term is None and other_current_term is None

    def __ne__(self, other):
        return not(self==other)

    def differentiate(self):
        new_poly = Polynomial(self._first_node.coefficient * self._first_node.exponent, self._first_node.exponent - 1)
        current_term = self._first_node.next
        while current_term is not None:
            new_poly._addTermInDescendingOrder(self.TermNode(current_term.coefficient * current_term.exponent, current_term.exponent - 1))
            current_term = current_term.next
        return new_poly

    def integrate(self):
        new_poly = Polynomial(self._first_node.coefficient / (self._first_node.exponent + 1), self._first_node.exponent + 1)
        current_term = self._first_node.next
        while current_term is not None:
            new_poly._addTermInDescendingOrder(self.TermNode(current_term.coefficient / (current_term.exponent + 1), current_term.exponent + 1))
            current_term = current_term.next
        return new_poly
