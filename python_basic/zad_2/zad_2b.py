def multiply_by_2_v1(list_of_numbers):  # v1 stands for version 1
    multiplied_list = []
    for number in list_of_numbers:
        number = number * 2
        multiplied_list.append(number)
    return multiplied_list


def multiply_by_2_v2(list_of_numbers):
    multiplied_list = [number * 2 for number in list_of_numbers]
    return multiplied_list


numbers = [1, 2, 5, 7, 10]
print("Version 1 (with 'normal' for):", multiply_by_2_v1(numbers))
print("Version 2 (with folded list):", multiply_by_2_v2(numbers))
