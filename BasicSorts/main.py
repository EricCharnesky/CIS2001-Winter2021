def insertion_sort(some_list):
    for index in range(1, len(some_list)):
        current_index = index
        while current_index > 0 and some_list[current_index] < some_list[current_index - 1]:
            temp = some_list[current_index]
            some_list[current_index] = some_list[current_index - 1]
            some_list[current_index - 1] = temp
            current_index -= 1

def selection_sort(some_list):
    for index in range(len(some_list) - 1 ):
        smallest_index = index
        for index_to_check in range(smallest_index+1, len(some_list)):
            if some_list[index_to_check] < some_list[smallest_index]:
                smallest_index = index_to_check
        temp = some_list[index]
        some_list[index] = some_list[smallest_index]
        some_list[smallest_index] = temp


def _binary_search(data, sorted_list, start_index, end_index):
    middle_index = ( start_index + end_index ) // 2
    if data == sorted_list[middle_index]:
        return middle_index
    if start_index == end_index:
        raise ValueError("not found!")
    if data < sorted_list[middle_index]:
        return _binary_search(data, sorted_list, start_index, middle_index - 1)
    return _binary_search(data, sorted_list, middle_index + 1, end_index)


def binary_search(data, sorted_list):
    return _binary_search(data, sorted_list, 0, len(sorted_list) - 1)



some_list = [ 10, 7, 5, 12, 3, 30, 20]

print(some_list)
insertion_sort(some_list)
print(some_list)

some_list = [ 10, 7, 5, 12, 3, 30, 20]

print(some_list)
selection_sort(some_list)
print(some_list)

for item in some_list:
    print(f'{item} was found at index: {binary_search(item, some_list)}')

binary_search(40, some_list)