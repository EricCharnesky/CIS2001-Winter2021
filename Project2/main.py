from Dock import Dock

input()
number_of_items_per_train_list = [ int(value) for value in input().split() ]
number_of_items_per_plane_list = [ int(value) for value in input().split() ]
train_item_list = [ int(value) for value in input().split() ]
plane_item_list = [ int(value) for value in input().split() ]

dock = Dock(number_of_items_per_train_list, number_of_items_per_plane_list,
            train_item_list, plane_item_list)

print(dock.get_train_load_times())
print(dock.get_plane_load_times())
