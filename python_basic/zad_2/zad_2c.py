def only_even_nums(range_func):
    for num in range_func:
        if num % 2 == 0:
            print(num)


only_even_nums(range(1, 11))
