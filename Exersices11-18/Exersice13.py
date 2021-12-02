def unique_items(list1, list2):
    print(list(set(list1) - set(list2)))


list1 = [1, 2, 3, 3, 4]
list2 = [1, 4, 5]
unique_items(list1, list2)
