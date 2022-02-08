class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(grade, int) and 0 <= grade <= 10 and isinstance(lecturer, Lecturer) and \
                course in lecturer.courses_attached and course in self.courses_in_progress:
            if course not in lecturer.grades:
                lecturer.grades[course] = []
            lecturer.grades[course].append(grade)

    def __str__(self):
        res = f"Имя: " + self.name + "\nФамилия: " + self.surname + \
               "\nСредняя оценка за домашние задания: " + str(avg(self.grades)) + \
               "\nКурсы в процессе изучения: " + ", ".join(self.courses_in_progress) + \
               "\nЗавершенные курсы: " + ", ".join(self.finished_courses) + "\n"
        return res

    def __ge__(self, other):
        res = avg(self.grades) >= avg(other.grades)
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f"Имя: " + self.name + "\nФамилия: " + self.surname + "\n"
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = super().__str__() + "Средняя оценка за лекции:" + str(avg(self.grades)) + "\n"
        return res

    def __lt__(self, other):
        res = avg(self.grades) < avg(other.grades)
        return res


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
        res = super().__str__()
        return res


def avg(grades):
    x = 0
    length = 0
    for value in grades.values():
        x = x + sum(value)
        length = length + len(value)
    res = round(x / length)
    return res


def students_course_rate(students, course):
    grades = []
    for student in students:
        if course in student.grades:
            grades += student.grades[course]
    res = avg({'grades': grades})
    return res


def lecturers_course_rate(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades += lecturer.grades[course]
    res = avg({'grades': grades})
    return res


some_student1 = Student('Sergey', 'Sidorov', 'Man')
some_student1.courses_in_progress = ['Java', 'Python']
some_student1.finished_courses = ['git']
some_student2 = Student('Elena', 'Sidorova', 'Woman')
some_student2.courses_in_progress = ['Python']
some_student2.finished_courses = ['git']

some_lecturer1 = Lecturer('Alexsandr', 'Efremov')
some_lecturer1.courses_attached = ['Java']
some_lecturer2 = Lecturer('Valera', 'Borisov')
some_lecturer2.courses_attached = ['Python']

some_reviewer1 = Reviewer('Nicolay', 'Haritonov')
some_reviewer1.courses_attached = ['Java']
some_reviewer2 = Reviewer('Konstantin', 'Timofeev')
some_reviewer2.courses_attached = ['Python']

some_reviewer1.rate_hw(some_student1, 'Java', 5)
some_reviewer1.rate_hw(some_student1, 'Python', 10)
some_reviewer1.rate_hw(some_student1, 'Java', 7)
some_reviewer1.rate_hw(some_student2, 'Python', 8)
some_reviewer1.rate_hw(some_student2, 'Python', 5)
some_reviewer1.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 7)
some_reviewer2.rate_hw(some_student2, 'Python', 6)
some_reviewer2.rate_hw(some_student1, 'Java', 8)
some_reviewer2.rate_hw(some_student1, 'Python', 9)
some_reviewer2.rate_hw(some_student1, 'Java', 3)

some_student1.rate_lecturer(some_lecturer1, 'Java', 8)
some_student1.rate_lecturer(some_lecturer2, 'Python', 10)
some_student1.rate_lecturer(some_lecturer2, 'Pyton', 8)
some_student2.rate_lecturer(some_lecturer1, 'Java', 5)
some_student2.rate_lecturer(some_lecturer2, 'Python', 8)
some_student1.rate_lecturer(some_lecturer1, 'Java', 5)
some_student1.rate_lecturer(some_lecturer2, 'Python', 4)
some_student2.rate_lecturer(some_lecturer1, 'Java', 8)
some_student1.rate_lecturer(some_lecturer1, 'Java', 4)
some_student1.rate_lecturer(some_lecturer2, 'Python', 8)
some_student1.rate_lecturer(some_lecturer2, 'Python', 9)
some_student2.rate_lecturer(some_lecturer1, 'Java', 9)
some_student1.rate_lecturer(some_lecturer1, 'Java', 10)

student_rate_python = students_course_rate([some_student1, some_student2], 'Python')
student_rate_java = students_course_rate([some_student1, some_student2], 'Java')
lecturer_rate_java = lecturers_course_rate([some_lecturer1], 'Java')
lecturer_rate_python = lecturers_course_rate([some_lecturer2], 'Python')

print(some_student1)
print(some_lecturer2)
print(some_reviewer2)
print(some_student1.__ge__(some_student2))
print(some_lecturer1.__lt__(some_lecturer2))
print('Средняя оценка студентов по курсу Python: ' + str(student_rate_python))
print('Средняя оценка студентов по курсу Java: ' + str(student_rate_java))
print('Средняя оценка лекторов по курсу Python: ' + str(lecturer_rate_python))
print('Средняя оценка лекторов по курсу Java: ' + str(lecturer_rate_java))





