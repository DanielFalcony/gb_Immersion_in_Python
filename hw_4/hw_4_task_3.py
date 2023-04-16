"""
Task 3

Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

bank_account = 0
count = 0
start = 0
operations = []


# Добавление денег и проверка на кратность 50
def add_money(money: int | float) -> int or float:
    while not money % 50 == 0:
        money = int(input('Банкомат принимает только суммы кратные 50 рублям,\n введите сумму заново ->: '))
        operation_logs((bank_account + money))
    return bank_account + money


# Снятие денег со счета, проверка на кратность 50 и процент за снятие.
def get_money(money: int | float) -> int or float:
    while not money % 50 == 0:
        money = int(input('Банкомат принимает только суммы кратные 50 рублям,\n введите сумму заново ->: '))
    if money <= 2_000:
        operation_logs(-(bank_account - money) - 30)
        return (bank_account - money) - 30
    elif 2_001 <= money <= 40_000:
        operation_logs(-(bank_account - money) * 0.985)
        return (bank_account - money) * 0.985
    else:
        operation_logs(-(bank_account - money) - 600)
        return (bank_account - money) - 600


# Выход из программы
def bank_exit():
    return f'Вы вышли!'


# Распечатать баланс счета
def print_bank() -> int or float:
    return f'На вашем счете: {bank_account} руб.'


# Проверка и списание налога на богатство (10%)
def check_bank(val):
    if val >= 5_000_000:
        val = val * 0.90
        return val, f'С Вас вычли 5% налога на богатство, баланс счета: {val}'
    else:
        return val, None


# Проверка корректности ввода
def check_input_value(val: str, flag=0) -> int:
    while isinstance(val, (int | float)):
        val = input('Банкомат принимает только Целые числа и числа с плавающей точкой, введите снова!\n'
                    '|--->: ')
    if flag == 1:
        while bank_account - int(val) < 0:
            val = input(f'У вас недостаточно денег для снятия! в банке {bank_account}!\n'
                        '|--->: ')
    return int(val)


# Счетчик операций и начисление процентов на остаток
def count_checker(count_cur, val):
    if count_cur < 2:
        count_cur += 1
        return count_cur, val
    if count_cur >= 2:
        count_cur = 0
        val = val * 1.03
        return count_cur, val, f'Начислены проценты!) Баланс счета: {val}'


def operation_logs(val: int | float) -> int or float:
    operations.append(val)


def show_log():
    return operations


# match/case пользовательского ввода
def user_choice(value: int) -> str:
    match value:
        case 1:
            return 'Пополнить счет'
        case 2:
            return 'Снять деньги со счета'
        case 3:
            return 'Проверить счет'
        case 4:
            return 'Выйти'
        case 5:
            return 'Посмотреть Лог операций'


# match/case работы программы ввода
def start_bank(value: str) -> int or float:
    match value:
        case 'Пополнить счет':
            money = input('Введите сумму для пополнения: ')
            money = check_input_value(money)
            return add_money(money)
        case 'Снять деньги со счета':
            money = input('Введите сумму для снятия: ')
            money = check_input_value(money, 1)
            return get_money(money)
        case 'Проверить счет':
            return print_bank()
        case 'Выйти':
            return bank_exit()
        case 'Посмотреть Лог операций':
            return show_log()


# Исполнительная часть
while True:
    start = int(input(f'{"Добро пожаловать в банк"}\n'
                      f'{"Вы в меню"}\n'
                      f'{"Введите цифру желаемой услуги"}\n'
                      f'1 - Пополнить счет\n'
                      f'2 - Снять деньги со счета\n'
                      f'3 - Вывести текущий баланс\n'
                      f'4 - Выйти из банкомата\n'
                      f'5 - Посмотреть Лог операций\n'
                      f'Вводить сюда ---->: '))
    bank_account, *_ = check_bank(bank_account)
    if _[0]:
        print(_[0])
    result = start_bank(user_choice(start))
    if start == 4:
        print(result)
        quit()
    elif start == 1 or start == 2:
        bank_account = result
        count, bank_account, *_ = count_checker(count, bank_account)
        if _:
            print(_[0])
    else:
        print(result)
