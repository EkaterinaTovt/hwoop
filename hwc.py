
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecturer (self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in Student.courses_in_progress:
            if course in lecturer.grade_lecturer:
                lecturer.grade_lecturer[course] += [grade]
            else:
                lecturer.grade_lecturer[course] = [grade]
        else:
            return 'Ошибка'
    
        
    def __grade_average__ (self, student, course):
        all_students = []
        all_grades = []
        if course in student.courses_in_progress and course in self.grades.values():
            for grades_av in self.grades.values():
                all_grades.append(grades_av)
            if len(all_grades) > 0:
                return sum(all_grades) / len(all_students)
            else:
                return 'Нет оценок'


    def __gt__(self, other):
        return self.__grade_average__()> other.__grade_average__()

    def __lt__(self, other):
        return self.__grade_average__()  < other.__grade_average__()

    def __eq__(self, other):
        return self.__grade_average__()  == other.__grade_average__()

    def __str__ (self):
        res = f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.__grade_average__() } \n Курсы в процессе изучения: {self.courses_in_progress} \n Завершенные курсы: {self.finished_courses}'
        return res

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_lecturer = {} 
        all_grades = []


    def __grade_average__ (self, lecturer, course):
        all_grades = []
        if course in lecturer.courses_attached and course in lecturer.grade_lecturer.values():
            for grades_av in self.grades.values():
                all_grades.append(grades_av)
            if len(all_grades) > 0:
                return sum(all_grades) / len(all_grades)
            else:
                return 'Нет оценок'


    def __gt__(self, other):
            return self.__grade_average__()  > other.__grade_average__()


    def __lt__(self, other):
            return self.__grade_average__() < other.__grade_average__()


    def __eq__(self, other):
            return self.__grade_average__()  == other.__grade_average__()
        

    def __str__ (self):
        res = f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.__grade_average__()}'



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__ (self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return res


student_1 = Student("Семен", "Слепаков", "м")
student_2 = Student("Сергей", "Светлаков", "м")
student_1.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Python']
student_1.finished_courses = ['Python']
student_2.finished_courses = ['Git']
print(student_1)
print(student_2)
first_reviewer = Reviewer("Дональд", "Дак")
second_reviewer = Reviewer("Майк", "Вазовски")
first_reviewer.courses_attached.append('Git')
second_reviewer.courses_attached.append('Python')
first_reviewer.rate_hw(student_1, "Git", 5)
first_reviewer.rate_hw(student_2, "Git", 10)
second_reviewer.rate_hw(student_1, "Python", 1)
second_reviewer.rate_hw(student_2, "Python", 2)
print(student_1)
print(student_2)
print('student_1 > student_2:', student_1 > student_2)
print('student_1 < student_2:', student_1 < student_2)
first_lecturer = Lecturer('Питер', 'Паркер')
second_lecturer = Lecturer('Майкл', 'Паркер')
first_lecturer.courses_attached.append('Python')
first_lecturer.courses_attached.append('JS')
second_lecturer.courses_attached.append('Git')
second_lecturer.courses_attached.append('C#')
student_1.rate_lecturer(first_lecturer, 'Python', 6)
student_2.rate_lecturer(first_lecturer, 'C#', 9)
student_1.rate_lecturer(second_lecturer, 'Git', 6)
student_2.rate_lecturer(second_lecturer, 'Java', 8)
print(first_lecturer)
print(second_lecturer)