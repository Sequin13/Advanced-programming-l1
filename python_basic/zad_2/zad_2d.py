import random


def only_second_num(list_of_nums):
    for i in range(0, len(list_of_nums)):
        if i % 2 == 1:
            print(list_of_nums[i])


numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)
only_second_num(numbers)
