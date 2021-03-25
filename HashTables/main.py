import sys
import random


class Student:

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def __hash__(self):
        # only want to hash immutable properties
        # reduce collisions - the goal is a uniform distribution
        return hash(self._name)
       # return 0 # don't try this at home, I'm a professional

    def __eq__(self, other):
        return type(self) == type(other) and \
               self._name == other._name and self._score == other._score

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

grades = {}

for letter in alphabet:
    for second_letter in alphabet:
        student = Student(letter + second_letter, 0)
        grades[student] = 0



eric = Student('EC', 0)

print(eric.__hash__())
print(hex(id(eric)))
print(eric)

another_eric = Student('EC', 0)

print(another_eric.__hash__())
print(hex(id(another_eric)))
print(another_eric)

print('grade for EC: ', grades[eric])