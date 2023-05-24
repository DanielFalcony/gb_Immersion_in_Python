from random import randint

"""
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь

"""


class People:
    def __init__(self, name: str, last_name: str, age: int):
        self.__name = name
        self.__last_name = last_name
        self.__age = age

    def birthday_up(self):
        self.__age += 1

    def age_getter(self):
        return self.__age

    def full_name_getter(self):
        return f'{self.__name} {self.__last_name}'


class Employee(People):
    def __init__(self, *args):
        super().__init__(*args)
        self.__emp_id = str(randint(10 ** 5, 10 ** 6))
        self.__access_level = sum(int(i) for i in self.__emp_id) % 7

    def id_getter(self):
        return self.__emp_id

    def access_level(self):
        return self.__access_level


man_1 = People('Федор', 'Пупкин', 25)
man_1.birthday_up()
man_1.birthday_up()
print(f'{man_1.age_getter()= }, {man_1.full_name_getter()= }')

man_2 = People('Иван', 'Жопкин', 20)
man_2.birthday_up()
man_2.birthday_up()
print(f'{man_2.age_getter()= }, {man_2.full_name_getter()= }')

empl_1 = Employee('Федор', 'Пупкин', 25)
print(f'{empl_1.full_name_getter()= },{empl_1.age_getter()= }, {empl_1.id_getter()= }, {empl_1.access_level()= }')
