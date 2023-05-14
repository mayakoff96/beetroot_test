class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def intro(self):
        print(f'Hello my name is {self.name}. I am {self.age} years old.')

    def study(self):
        print('I am studying on the course of Python.')


class Student(Person):

    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender)
        self.grade = grade

    def intro(self):
        super().intro()
        print(f'I am in grade {self.grade}')

    def class_attending(self):
        print('I am attending class.')

    def homework(self):
        print('I am doing homework')


class Teacher(Person):

    def __init__(self, name, age, gender, salary, subject):
        super().__init__(name, age, gender)
        self.salary = salary
        self.subject = subject

    def intro(self):
        super().intro()
        print(f'I am a teacher with a salary of ${self.salary}')

    def teach_the_subject(self):
        print(f'I am teaching the subject {self.subject}')

    def grade_exam(self):
        print('I am grading exams')


# Person
person = Person('Dmytro', 27, 'Male')
person.intro()
person.study()
# Student
student = Student('Anna', 14, 'Female', 11)
student.intro()
student.class_attending()
student.homework()
# Teacher
teacher = Teacher('Mr. Valintine', 35, 'Male', 5500, 'Math')
teacher.intro()
teacher.teach_the_subject()
teacher.grade_exam()