class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        if self.finished_courses == []:
            p = 'Завершенные курсы: Введение в программирование'
        else:
            p = f'Завершенные курсы: {", ".join(self.courses_in_progress)}'
        courses_in_progress = ", ".join(self.courses_in_progress)
        grade_sum = 0
        len_grade = []
        for grade in self.grades.values():
            for grade_1 in grade:
                grade_sum += grade_1
                len_grade.append(grade_1)
        grade = round(grade_sum / len(len_grade), 1)
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {grade} \nКурсы в процессе изучения: {courses_in_progress} \n{p}'
        return res
    def __lt__(self, other):
        grade_sum = 0
        len_grade = []
        for grade in self.grades.values():
            for grade_1 in grade:
                grade_sum += grade_1
                len_grade.append(grade_1)
        grade_other = 0
        len_grade_other = []
        for grade_4 in other.grades.values():
            for grade_3 in grade_4:
                grade_other += grade_3
                len_grade_other.append(grade_3)
        if not isinstance(other, Student) or not isinstance(self, Student):
            print('Not Student')
            return
        elif round(grade_sum / len(len_grade), 1) == round(grade_other / len(len_grade_other), 1):
            res = f'{self.name} {self.surname} имеет такую же среднюю оценку'
            return res
        elif (round(grade_sum / len(len_grade), 1) > round(grade_other / len(len_grade_other), 1)) == True:
            res = f'{self.name} {self.surname} имеет среднюю оценку выше'
            return res
        elif (round(grade_sum / len(len_grade), 1) > round(grade_other / len(len_grade_other), 1)) == False:
            res = f'{self.name} {self.surname} имеет среднюю оценку ниже'
            return res
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
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
        n = f'Имя: {self.name} \nФамилия: {self.surname}'
        return n
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_in_progress = []
    def __str__(self):
        grade_sum = 0
        len_grade = []
        for grade in self.grades.values():
            for grade_1 in grade:
                grade_sum += grade_1
                len_grade.append(grade_1)
        grade = round(grade_sum / len(len_grade), 1)
        n = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {grade}'
        return n
    def __lt__(self, other):
        grade_sum = 0
        len_grade = []
        for grade in self.grades.values():
            for grade_1 in grade:
                grade_sum += grade_1
                len_grade.append(grade_1)
        grade_other = 0
        len_grade_other = []
        for grade_4 in other.grades.values():
            for grade_3 in grade_4:
                grade_other += grade_3
                len_grade_other.append(grade_3)
        if not isinstance(other, Lecturer) or not isinstance(self, Lecturer):
            print('Not Lecturer')
            return
        elif round(grade_sum / len(len_grade), 1) == round(grade_other / len(len_grade_other), 1):
            res = f'{self.name} {self.surname} имеет такой же рейтинг'
            return res
        elif (round(grade_sum / len(len_grade), 1) > round(grade_other / len(len_grade_other), 2)) == True:
            res = f'{self.name} {self.surname} имеет рейтинг больше'
            return res
        elif (round(grade_sum / len(len_grade), 1) > round(grade_other / len(len_grade_other), 1)) == False:
            res = f'{self.name} {self.surname} имеет рейтинг меньше'
            return res
    def lw_rating(self, course):
        if course in self.courses_in_progress or course in self.courses_attached:
            grade = round(sum(self.grades.values()) / len(self.grades.values()), 1)
            return grade
        else:
            print('Not found')

def grade_hw(student, courses):
    grades = []
    keys = []
    key = []
    for stud in student:
        if courses in stud.grades.keys():
            keys.append(stud.grades.values())
            grades.append(stud.grades.values())
    grade_sum = 0
    for grade in grades:
        for grade_1 in grade:
            for grade_2 in grade_1:
                grade_sum += grade_2
    for key_1 in keys:
        for key_2 in key_1:
            for key_3 in key_2:
                key.append(key_3)
    print(f'Средняя оценка домашнего задания по курсу {courses}: {round(grade_sum / len(key), 1)}')

def grade_lw(lectors, courses):
    grades = []
    keys = []
    key = []
    for lector in lectors:
        if courses in lector.grades.keys():
            keys.append(lector.grades.values())
            grades.append(lector.grades.values())
    grade_sum = 0
    for grade in grades:
        for grade_1 in grade:
            for grade_2 in grade_1:
                grade_sum += grade_2
    for key_1 in keys:
        for key_2 in key_1:
            for key_3 in key_2:
                key.append(key_3)
    print(f'Средняя оценка лекции по курсу {courses}: {round(grade_sum / len(key), 1)}')




some_lector_1 = Lecturer('Andrey', 'Shestakov')
some_lector_2 = Lecturer('Anatoliy', 'Griboedov')
some_lector_3 = Lecturer('Olga', 'Zdor')
some_lector_4 = Lecturer('Inokenty', 'Roshenko')

some_lector_1.courses_in_progress.append('Phyton')
some_lector_2.courses_in_progress.append('Jar')
some_lector_3.courses_in_progress.append('Phyton')
some_lector_4.courses_in_progress.append('Phyton')




some_student_1 = Student('Viktoria', 'Mokrousova', 'Woman')
some_student_2 = Student('Alian', 'Alkema', 'Woman')
some_student_3 = Student('Dmitriy', 'Alkema', 'Man')
some_student_4 = Student('Vladislav', 'Grechin', 'Man')

some_student_1.rate_lw(some_lector_1, 'Phyton', 7)
some_student_1.rate_lw(some_lector_1, 'Phyton', 6)
some_student_1.rate_lw(some_lector_1, 'Phyton', 7)
some_student_2.rate_lw(some_lector_2, 'Jar', 10)
some_student_2.rate_lw(some_lector_2, 'Jar', 6)
some_student_2.rate_lw(some_lector_2, 'Jar', 3)
some_student_2.rate_lw(some_lector_2, 'Jar', 1)
some_student_2.rate_lw(some_lector_2, 'Jar', 7)

some_student_3 = Student('Dmitriy', 'Alkema', 'Man')
some_student_4 = Student('Vladislav', 'Grechin', 'Man')

stu_1 = {'Phyton': [2]}
stu_2 = {'Jar': [5]}
stu_3 = {'Phyton': [9]}
stu_4 = {'Jar': [7]}

some_student_1.grades.update(stu_1)
some_student_2.grades.update(stu_2)
some_student_3.grades.update(stu_3)
some_student_4.grades.update(stu_4)

some_student_1.courses_in_progress.append('Phyton')
some_student_1.courses_in_progress.append('Jar')
some_student_2.courses_in_progress.append('Jar')
some_student_2.courses_in_progress.append('Phyton')
some_student_3.courses_in_progress.append('Phyton')
some_student_4.courses_in_progress.append('Phyton')




some_rewiewer_1 = Reviewer('Olga', 'Kapranova')
some_rewiewer_2 = Reviewer('Alexey', 'Safonov')

some_rewiewer_1.courses_attached.append('Phyton')
some_rewiewer_2.courses_attached.append('Jar')
some_rewiewer_2.courses_attached.append('Phyton')

some_rewiewer_1.rate_hw(some_student_1, 'Phyton', 3)
some_rewiewer_1.rate_hw(some_student_1, 'Phyton', 7)
some_rewiewer_1.rate_hw(some_student_1, 'Phyton', 10)
some_rewiewer_2.rate_hw(some_student_2, 'Jar', 6)
some_rewiewer_2.rate_hw(some_student_2, 'Phyton', 2)
some_rewiewer_2.rate_hw(some_student_2, 'Jar', 8)


list_students = [some_student_1, some_student_2, some_student_3, some_student_4]
list_lecturer = [some_lector_1, some_lector_2, some_lector_3, some_lector_4]

grade_hw(list_students, 'Phyton')
grade_lw(list_lecturer, 'Phyton')
print(some_rewiewer_1)
print(some_student_1)
print(some_lector_1)
print(some_lector_1 > some_lector_2)
print(some_student_1 < some_student_2)



