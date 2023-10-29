class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        CIP = ", ".join(self.courses_in_progress)
        CF = ", ".join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{average_grade(self.grades.values())}\nКурсы в процессе изучения: {CIP}\nЗавершенные курсы: {CF}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        # Тут не нашёл другого решения, кроме добавления словаря "grades" в родительский класс. Ещё можно было добавить def __init__
        # в класс "Lecturer", но тогда получится совсем непрактично. Если оставить словарь с оценками в дочернем классе "Lecturer", то словарь будет
        # одинаковым для всех объектов класса "Lecturer"

class Lecturer(Mentor):

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{average_grade(self.grades.values())}"

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def average_grade(grades):
    all_grades = []
    for lst in grades:
        for el in lst:
            all_grades.append(el)
    return sum(all_grades)/len(all_grades)

def compare_students(student1, student2):
    if average_grade(student1.grades.values()) > average_grade(student2.grades.values()):
        return f"У студента \"{student1.name} {student1.surname}\" средний балл больше, чем у студента \"{student2.name} {student2.surname}\""
    elif average_grade(student1.grades.values()) < average_grade(student2.grades.values()):
        return f"У студента \"{student1.name} {student1.surname}\" средний балл меньше, чем у студента \"{student2.name} {student2.surname}\""
    else:
        return f"У студента \"{student1.name} {student1.surname}\" средний балл такой же, как у студента \"{student2.name} {student2.surname}\""

def compare_lecturers(lecturer1, lecturer2):
    if average_grade(lecturer1.grades.values()) > average_grade(lecturer2.grades.values()):
        return f"У лектора \"{lecturer1.name} {lecturer1.surname}\" средний балл больше, чем у лектора \"{lecturer2.name} {lecturer2.surname}\""
    elif average_grade(lecturer1.grades.values()) < average_grade(lecturer2.grades.values()):
        return f"У лектора \"{lecturer1.name} {lecturer1.surname}\" средний балл меньше, чем у лектора \"{lecturer2.name} {lecturer2.surname}\""
    else:
        return f"У лектора \"{lecturer1.name} {lecturer1.surname}\" средний балл такой же, как у лектора \"{lecturer2.name} {lecturer2.surname}\""

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.courses_in_progress += ['Введение в программирование']

bad_student = Student('Eric', 'Harris', 'male')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Git']
bad_student.courses_in_progress += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.courses_attached += ['Введение в программирование']
 
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Введение в программирование', 10)

bad_reviewer = Reviewer('Sf', 'Na mide')
bad_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['Git']
bad_reviewer.courses_attached += ['Введение в программирование']

bad_reviewer.rate_hw(bad_student, 'Python', 2)
bad_reviewer.rate_hw(bad_student, 'Git', 3)
bad_reviewer.rate_hw(bad_student, 'Введение в программирование', 2)

cool_lecturer = Lecturer('Some', 'Body')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
cool_lecturer.courses_attached += ['Введение в программирование']

bad_lecturer = Lecturer('So', 'Cold')
bad_lecturer.courses_attached += ['Python']
bad_lecturer.courses_attached += ['Git']
bad_lecturer.courses_attached += ['Введение в программирование']

best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Git', 9)
best_student.rate_lecture(cool_lecturer, 'Введение в программирование', 10)

bad_student.rate_lecture(bad_lecturer, 'Python', 1)
bad_student.rate_lecture(bad_lecturer, 'Git', 3)
bad_student.rate_lecture(bad_lecturer, 'Введение в программирование', 2)

print(cool_reviewer)
print(best_student)
print(bad_student)
print(compare_students(best_student, bad_student))
print(cool_lecturer)
print(bad_lecturer)
print(compare_lecturers(cool_lecturer, bad_lecturer))

print(list(best_student.grades.values()))
print(list(cool_lecturer.grades.values()))
print(list(bad_student.grades.values()))
print(list(bad_lecturer.grades.values()))

