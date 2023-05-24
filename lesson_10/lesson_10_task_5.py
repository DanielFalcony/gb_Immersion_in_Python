"""
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.

"""


class Animals:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def about(self):
        return f'{self.__name}, {self.__age}'


class Fish(Animals):
    def __init__(self, *args):
        super().__init__(*args)
        self.__swim = 'Буль-буль'

    def what_doing(self):
        return self.__swim


class Dog(Animals):
    def __init__(self, *args):
        super().__init__(*args)
        self.__voice = 'Гав-Гав'

    def what_doing(self):
        return self.__voice


class Cat(Animals):
    def __init__(self, *args):
        super().__init__(*args)
        self.__kitty = 'Мяу-мяу'

    def what_doing(self):
        return self.__kitty


cat = Cat('hello_kitty', 3)
print(f'{cat.about()= }, {cat.what_doing()= }')

dog = Dog('doggy_dog', 5)
print(f'{dog.about()= }, {dog.what_doing()= }')

fish = Fish('Dorry', 1)
print(f'{fish.about()= }, {fish.what_doing()= }')
