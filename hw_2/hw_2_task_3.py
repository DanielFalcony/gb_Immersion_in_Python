from math import gcd

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""

number_one = input('Введите первое значение формата "2/5": ')
number_two = input('Введите второе значение формата "2/5": ')
number_one_list = []
number_two_list = []


def get_numbers(number):
    if '/' in number:
        val = number.split('/')
        val_list = []
        for i in val:
            val_list.append(int(i))
        return val_list
    else:
        return 'Введены неверные данные!'


def get_multiplication(val_1, val_2):
    number_one_list = get_numbers(val_1)
    number_two_list = get_numbers(val_2)
    if number_one_list[0] == 0 or number_two_list[0] == 0:
        return 'Дробь равна Нулю!'
    else:
        val_1 = number_one_list[0] * number_two_list[0]
        val_2 = number_one_list[1] * number_two_list[1]
        val_1, val_2 = str(val_1), str(val_2)
        return f'{number_one} * {number_two} = {val_1}/{val_2}'


def get_summ(val_1, val_2):
    number_one_list = get_numbers(val_1)
    number_two_list = get_numbers(val_2)
    num_1, den_1 = number_one_list[0], number_one_list[1]
    num_2, den_2 = number_two_list[0], number_two_list[1]
    lcm = den_1 * den_2 // gcd(den_1, den_2)
    num_summ = num_1 * (lcm // den_1) + num_2 * (lcm // den_2)
    return f'{number_one} + {number_two} = {num_summ}/{lcm}'


print(get_multiplication(number_one, number_two))
print(get_summ(number_one, number_two))
