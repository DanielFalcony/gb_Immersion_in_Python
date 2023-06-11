"""
Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
"""


class Animals:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def about(self):
        return f'{self.__name}, {self.__age}'


class Fish(Animals):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__name = name
        self.__age = age
        self.__type = 'Рыба'
        self.__swim = 'Буль-буль'

    def what_doing(self):
        return self.__swim

    def about(self):
        return f'{self.__type}, {self.__name}, {self.__age}, {self.__swim}'


class Dog(Animals):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__name = name
        self.__age = age
        self.__type = 'Собака'
        self.__voice = 'Гав-Гав'

    def what_doing(self):
        return self.__voice

    def about(self):
        return f'{self.__type}, {self.__name}, {self.__age}, {self.__voice}'


class Cat(Animals):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__name = name
        self.__age = age
        self.__type = 'Кошка'
        self.__kitty = 'Мяу-мяу'

    def what_doing(self):
        return self.__kitty

    def about(self):
        return f'{self.__type}, {self.__name}, {self.__age}, {self.__kitty}'


class AnimalsFactory:
    def __init__(self, anim: str, name: str, age: int):
        self.__anim = anim.title()
        self.__name = name
        self.__age = age

    def create_animal(self):
        if self.__anim == 'Fish':
            return Fish(self.__name, self.__age)
        elif self.__anim == 'Dog':
            return Dog(self.__name, self.__age)
        elif self.__anim == 'Cat':
            return Cat(self.__name, self.__age)
        else:
            return f'Такого класса {self.__anim} нет!'


animal_1 = AnimalsFactory('Dog', 'Лунтик', 2).create_animal()
animal_2 = AnimalsFactory('Cat', 'Фунтик', 3).create_animal()
animal_3 = AnimalsFactory('Fish', 'Фугу', 4).create_animal()
animal_4 = AnimalsFactory('Chicken', 'Коко', 5).create_animal()
print(f'{animal_1.about()=}\n{animal_2.about()=}\n{animal_3.about()=}\n{animal_4}')
