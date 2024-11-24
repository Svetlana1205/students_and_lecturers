class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture (self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if  0 < grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return "Поставьте оценку в диапазоне от 1 до 10"
        else:
            return "Ошибка"

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade (self):
        if self.grades:  # Проверка, есть ли оценки
            all_grades = []  # Создаем список для всех оценок
            for grades_list in self.grades.values():
                all_grades.extend(grades_list)  # Добавляем все оценки в один список
            return sum(all_grades) / len(all_grades)  # Считаем среднее значение
        else:
            return "Оценки ещё не проставлены"

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_homework (self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

inspector = Reviewer("Georg", "Katunin")
# print(inspector)
lecturer1 = Lecturer("Svetlana", "Katunina")
lecturer1.courses_attached += ['Python']
best_student = Student('Ruoy', 'Eman', 'male')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

best_student.rate_lecture(lecturer1, "Python", 10)
best_student.rate_lecture(lecturer1, "Python", 10)
best_student.rate_lecture(lecturer1, "Python", 7)
# print(lecturer1.average_grade())
print(lecturer1)
