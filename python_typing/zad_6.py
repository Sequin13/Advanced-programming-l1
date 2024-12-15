def operations_on_lists(first_list: list, scnd_list: list) -> list:
    return [num ** 3 for num in list(set(first_list + scnd_list))]


l1 = [3, 2, 3, 4, 5, 6, 7, 8, 8, 9]
l2 = [6, 7, 2, 1, 6, 1, 5, 3, 10, 11, 57]
print(operations_on_lists(l1, l2))
