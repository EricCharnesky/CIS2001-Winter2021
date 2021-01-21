import copy

from ball import Ball
from Item import Item
from TaxableItem import TaxableItem


class Numbers:

    def __init__(self, first, second, third):
        self.numbers = [first, second, third]


def juggle(ball1, ball2, ball3):
    ball1.catch()
    ball2.catch()
    ball3.toss()

    ball1.toss()
    ball3.catch()

    ball2.toss()
    ball1.catch()


basketball = Ball("Basketball")
basketball.toss()
baseball = Ball("Baseball")
baseball.toss()
raquetball = Ball("Raquetball")
raquetball.toss()

juggle(basketball, baseball, raquetball)

print(basketball)
print(baseball)
print(raquetball)


nachos = Item("Nacho", 2.5, 3)

beer = TaxableItem("12 pack of generic beer", 10, 1, .06)

first_set = Numbers(1,2,3)
second_set = Numbers(4,5,6)


# alias - two variables pointed to the same object
third_set = first_set

# actual copy
third_set = copy.deepcopy(first_set)

print(first_set.numbers)
print(second_set.numbers)
print(third_set.numbers)

first_set.numbers[0] = 20

print(first_set.numbers)
print(second_set.numbers)
print(third_set.numbers)

# don't access "private" values directly
# basketball._is_moving = True
