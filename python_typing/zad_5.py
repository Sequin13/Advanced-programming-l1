def is_list_contains(list_of_nums: list, num: int) -> bool:
    return num in list_of_nums


list_of_nums = [1, 2, 3, 4, 5, 10, 11, 12]
num_to_check = 4
print(is_list_contains(list_of_nums, num_to_check))
