"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def fibo(val: int) -> int:
    return 1 if val in (1, 2) else fibo(val - 1) + fibo(val - 2)


print(fibo(15))
