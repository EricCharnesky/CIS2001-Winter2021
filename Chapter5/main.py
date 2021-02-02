import sys

import random

some_list = []

for n in range(1,1001):
    some_list.append(n)
    print(f"Size of list with {n} items: {sys.getsizeof(some_list)}")


random_list = []

for n in range(1000):
    random_list.append(random.randint(1,1_000_000))

for number in random_list:
    if number == 7321:
        print("found it!")


for index in range(len(random_list)):
    repeat_count = 0
    for index_to_check in range(0, index):
        if random_list[index_to_check] == random_list[index]:
            repeat_count += 1
    for index_to_check in range(index+1, len(random_list)):
        if random_list[index_to_check] == random_list[index]:
            repeat_count += 1
    if repeat_count > 0:
        print(f"found {repeat_count} instances of {random_list[index]}")

