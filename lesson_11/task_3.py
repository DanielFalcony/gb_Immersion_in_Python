"""
Задание №5
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.

Задание №6
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""


class Rectangle:
    def __init__(self, side_a: int, side_b: int | None = None):
        self.side_a = side_a
        self.side_b = side_b if side_b else side_a

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def rec_sqr(self):
        return self.side_a * self.side_b

    def __add__(self, other):
        # ratio = self.side_a / self.side_b
        # get_perimetr = self.perimeter() + other.perimeter()
        # return Rectangle((get_perimetr / 2) * ratio, (get_perimetr / 2) - (get_perimetr / 2) * ratio)
        return Rectangle(self.side_a + other.side_a, self.side_b + other.side_b)

    def __sub__(self, other):
        return Rectangle(abs(self.side_a - other.side_a), abs(self.side_b - other.side_b))

    def __lt__(self, other):
        return self.perimeter() < other.perimeter()

    def __le__(self, other):
        return self.perimeter() <= other.perimeter()

    def __eq__(self, other):
        return self.perimeter() == other.perimeter()

    def __str__(self):
        return f'Прямоугольник со сторонами {self.side_a}, {self.side_b} и периметром {self.perimeter()}'


if __name__ == '__main__':
    rec_1 = Rectangle(2, 3)
    rec_2 = Rectangle(2, 3)
    rec_3 = rec_1 + rec_2
    print(rec_3)

    rec_4 = Rectangle(4, 5)
    rec_5 = Rectangle(2, 3)
    rec_6 = rec_4 - rec_5
    print(rec_6)

    rec_7 = Rectangle(2, 2)
    rec_8 = Rectangle(3, 3)
    print(rec_7 > rec_8)
    print(rec_7 < rec_8)
    print(rec_7 >= rec_8)
    print(rec_7 <= rec_8)
    print(rec_7 == rec_8)
    print(rec_7 != rec_8)
