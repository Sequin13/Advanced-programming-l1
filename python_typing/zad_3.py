def is_even_or_odd(num: int) -> bool:
    return num % 2 == 0

num = 7
print("Liczba parzysta") if is_even_or_odd(num) else print("Liczba nieparzysta")

