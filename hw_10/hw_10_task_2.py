"""
Task 2

Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.

Дорабатываем задачу про банкомат.
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


class ATM:
    """
    Класс банкомат
    """
    bank_account = 0
    count = 0
    start = 0
    operations = []

    def __init__(self, money: int | float = 0):
        """
        Инициализация класса
        :param money: int|float
        """
        self.money = money

    def operation_logs(self, val: int | float):
        """
        Сохраняет информацию об операциях в банкомате в operations
        :param val: int|float
        :return: None
        """
        self.operations.append(val)

    # Добавление денег и проверка на кратность 50
    def add_money(self, money: int | float):
        """
        Пополнение банкомата
        :param money: int|float
        :return: None
        """
        while not money % 50 == 0:
            money = int(input('Банкомат принимает только суммы кратные 50 рублям,\n введите сумму заново ->: '))
        self.operation_logs(self.bank_account + money)
        self.bank_account += money

    # Снятие денег со счета, проверка на кратность 50 и процент за снятие.
    def get_money(self, money: int | float):
        """
        Снятие денег из банкомата
        :param money: int|float
        :return: None
        """
        while not money % 50 == 0:
            money = int(input('Банкомат принимает только суммы кратные 50 рублям,\n введите сумму заново ->: '))
        if money <= 2_000:
            self.bank_account = (self.bank_account - money) - 30
            self.operation_logs(-self.bank_account)
        elif 2_001 <= money <= 40_000:
            self.bank_account = (self.bank_account - money) * 0.985
            self.operation_logs(-self.bank_account)
        else:
            self.bank_account = (self.bank_account - money) - 600
            self.operation_logs(self.bank_account)

    # Выход из программы
    @staticmethod
    def bank_exit():
        """
        Статический метод завершения работы с банкоматом
        :return: str
        """
        return f'Вы вышли!'

    # Распечатать баланс счета
    def print_bank(self):
        """
        Выводит информацию о счете в банкомате
        :return: str
        """
        return f'На вашем счете: {self.bank_account} руб.'

    # Проверка и списание налога на богатство (10%)
    def check_bank(self):
        """
        Проверка налога на богатство при сумме на счете более 5 млн. (10%)
        :return: None
        """
        if self.bank_account >= 5_000_000:
            self.bank_account = self.bank_account * 0.90
            return self.bank_account, f'С Вас вычли 10% налога на богатство, баланс счета: {self.bank_account}'
        else:
            return self.bank_account, None

    # Проверка корректности ввода
    def check_input_value(self, val: str, flag=0) -> int:
        """
        Проверка корректности ввода данных
        :param val: int|float
        :param flag: int
        :return: int
        """
        while isinstance(val, (int | float)):
            val = input('Банкомат принимает только Целые числа и числа с плавающей точкой, введите снова!\n'
                        '|--->: ')
        if flag == 1:
            while self.bank_account - int(val) < 0:
                val = input(f'У вас недостаточно денег для снятия! в банке {self.bank_account}!\n'
                            '|--->: ')
        return int(val)

    # Счетчик операций и начисление процентов на остаток
    def count_checker(self, count_cur):
        """
        Счетчик операций и начисление процентов на остаток
        :param count_cur: int
        :return: None
        """
        if count_cur < 2:
            self.count += 1
            return self.count, self.bank_account
        if count_cur >= 2:
            self.count = 0
            self.bank_account = self.bank_account * 1.03
            return self.bank_account, self.bank_account, f'Начислены проценты!) Баланс счета: {self.bank_account}'

    def show_log(self):
        """
        Выводит лог операций по счету
        :return:
        """
        return self.operations

    # match/case пользовательского ввода
    @staticmethod
    def user_choice(value: int):
        """
        'match/case' - выборы пользователя
        :param value: int
        :return: str
        """
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
    def start_bank(self, value: str):
        """
        'match/case' - пользовательских выборов
        :param value: str
        :return: int|float
        """
        match value:
            case 'Пополнить счет':
                money = input('Введите сумму для пополнения: ')
                money = self.check_input_value(money)
                return self.add_money(money)
            case 'Снять деньги со счета':
                money = input('Введите сумму для снятия: ')
                money = self.check_input_value(money, 1)
                return self.get_money(money)
            case 'Проверить счет':
                return self.print_bank()
            case 'Выйти':
                return self.bank_exit()
            case 'Посмотреть Лог операций':
                return self.show_log()

    # Исполнительная часть


if __name__ == '__main__':

    my_bank = ATM(0)

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
        my_bank.bank_account, *_ = my_bank.check_bank()
        if _[0]:
            print(_[0])
        result = my_bank.start_bank(my_bank.user_choice(start))
        if start == 4:
            print(result)
            quit()
        elif start == 1 or start == 2:
            bank_account = result
            count, *_ = my_bank.count_checker(my_bank.count)
            if _:
                print(_[0])
        else:
            print(result)
