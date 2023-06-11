"""
Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами
отрицательной длины.

Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""

from error import RectangleTypeError, RectangleValueError


class Rectangle:
    def __init__(self, side_a: int, side_b: int | None = None):
        self.check_side(side_a)
        if side_b:
            self.check_side(side_b)
        self.side_a = side_a
        self.side_b = side_b if side_b else side_a

    @staticmethod
    def check_side(value):
        if not isinstance(value, int):
            raise RectangleTypeError(value)
        if value < 0:
            raise RectangleValueError(value)

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def rec_sqr(self):
        return self.side_a * self.side_b


if __name__ == '__main__':
    rec_1 = Rectangle(3, 5)
    print(f'{rec_1.perimeter()= }, {rec_1.rec_sqr()= }')
    rec_2 = Rectangle(3)
    print(f'{rec_2.perimeter()= }, {rec_2.rec_sqr()= }')
    rec_3 = Rectangle('Мое значение', -4)
    print(f'{rec_3.perimeter()= }, {rec_3.rec_sqr()= }')