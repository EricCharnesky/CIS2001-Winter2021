from matplotlib import pyplot as plt

import time


def compute_time_to_add(list_to_add_to, item):
    start = time.perf_counter()
    list_to_add_to.append(item)
    end = time.perf_counter()
    return end-start


def compute_time_to_remove_from_index(list_to_remove_from, index_to_remove_from):
    start = time.perf_counter()
    list_to_remove_from.pop(index_to_remove_from)
    end = time.perf_counter()
    return end - start


def compute_time_to_insert_at_index(list_to_insert_into, index_to_insert_into):
    start = time.perf_counter()
    list_to_insert_into.insert(index_to_insert_into, index_to_insert_into) # index, then value to add, the value doesn't matter
    end = time.perf_counter()
    return end - start


#timings = []
#some_list = []
#values = range(10_000_000)
#for n in values:
#    timings.append(compute_time_to_add(some_list, n))

# timings = []
# size_of_list = []
# memory_size_of_list = []
# values = list(range(100_000))
# for n in range(len(values)):
#     size_of_list.append(len(values))
#     timings.append(compute_time_to_remove_from_index(values, 0))
#     memory_size_of_list.append(sys.getsizeof(values))

timings = []
some_list = []
length_of_list = []

for n in range(100_000):
    length_of_list.append(len(some_list))
    timings.append(compute_time_to_insert_at_index(some_list, n))

plt.plot(length_of_list, timings)
plt.plot(list(range(1000)), list(range(1000)))
plt.show()

#plt.plot(size_of_list, timings)
#plt.plot(size_of_list, memory_size_of_list)
#plt.show()
