"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.
"""
import os
import csv


class NameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not value:
            raise ValueError(f"{self.name} Не может быть пустым!")
        if not value.isalpha():
            raise ValueError(f"{self.name} Должно содержать только буквы!")
        if not value.istitle():
            raise ValueError(f"{self.name} Должно начинаться с заглавной буквы!")
        instance.__dict__[self.name] = value


class Student:
    first_name = NameValidator()
    last_name = NameValidator()
    patronymic = NameValidator()

    def __init__(self, first_name, last_name, patronymic, subjects_csv):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.subjects = self.load_subjects(subjects_csv)
        self.scores = {subject: {'grades': [], 'test_scores': []} for subject in self.subjects}

    def __str__(self):
        return f'Оценки студента {self.first_name + " " + self.last_name + " " + self.patronymic}:\n' \
               f'{"*" * 30}\n' \
               f'Средняя оценка и балл студента: \n' \
               f'Math: {student.average_grade("Math")}, {student.average_test_score("Math")}\n' \
               f'Physics: {student.average_grade("Physics")}, {student.average_test_score("Physics")}\n' \
               f'Chemistry: {student.average_grade("Chemistry")}, {student.average_test_score("Chemistry")}\n' \
               f'English: {student.average_grade("English")}, {student.average_test_score("English")}\n ' \
               f'{"*" * 30}\n' \
               f'Средняя оценка по всем предметам: {student.overall_average_grade()}\n' \
               f'Средний балл по всем предметам: {student.overall_average_test_score()}\n' \
               f'{"*" * 30}\n' \


    @staticmethod
    def load_subjects(subjects_csv):
        if not os.path.exists(subjects_csv):
            subjects = ["Math", "Physics", "Chemistry", "English"]
            with open("subjects.csv", "w") as file:
                file.write("\n".join(subjects))
        with open(subjects_csv, 'r') as file:
            reader = csv.reader(file)
            subjects = [row[0] for row in reader]
        return subjects

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"{subject} Такого предмета нет!")
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть между 2 и 5")
        self.scores[subject]['grades'].append(grade)

    def add_test_score(self, subject, score):
        if subject not in self.subjects:
            raise ValueError(f"{subject} Такого предмета нет!")
        if score < 0 or score > 100:
            raise ValueError("Баллы по тесту могут быть между 0 и 100!")
        self.scores[subject]['test_scores'].append(score)

    def average_grade(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"{subject} Такого предмета нет!")
        grades = self.scores[subject]['grades']
        if not grades:
            return None
        return sum(grades) / len(grades)

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"{subject} Такого предмета нет!")
        scores = self.scores[subject]['test_scores']
        if not scores:
            return None
        return sum(scores) / len(scores)

    def overall_average_grade(self):
        grades = [grade for subject_scores in self.scores.values() for grade in subject_scores['grades']]
        if not grades:
            return None
        return sum(grades) / len(grades)

    def overall_average_test_score(self):
        scores = [score for subject_scores in self.scores.values() for score in subject_scores['test_scores']]
        if not scores:
            return None
        return sum(scores) / len(scores)


# Создание экземпляра студента
student = Student("Петр", "Иванович", "Иванов", "subjects.csv")
student_1 = Student("Виктор", "Дмитриевич", "Кузьминов", "subjects.csv")

# Добавление оценок и результатов тестов
student.add_grade('Math', 4)
student.add_grade('Math', 5)
student.add_grade('Physics', 3)
student.add_grade('Physics', 4)
student.add_grade('Chemistry', 2)
student.add_grade('Chemistry', 4)
student.add_grade('English', 5)
student.add_grade('English', 4)
student.add_test_score('Math', 90)
student.add_test_score('Physics', 60)
student.add_test_score('Chemistry', 75)
student.add_test_score('Chemistry', 95)
student.add_test_score('English', 60)

student_1.add_grade('Math', 4)
student_1.add_grade('Math', 3)
student_1.add_grade('Math', 3)
student_1.add_grade('Physics', 2)
student_1.add_grade('Physics', 5)
student_1.add_grade('Chemistry', 4)
student_1.add_grade('Chemistry', 3)
student_1.add_grade('English', 4)
student_1.add_grade('English', 4)
student_1.add_test_score('Math', 95)
student_1.add_test_score('Physics', 65)
student_1.add_test_score('Chemistry', 70)
student_1.add_test_score('Chemistry', 84)
student_1.add_test_score('English', 68)


print(student)
print(student_1)
