# -*- coding: utf-8 -*-

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50


# Przykładowe dane
student1 = Student("Jan Kowalski", [60, 70, 80, 90])
student2 = Student("Anna Nowak", [40, 30, 20, 10])

# Testowanie metody is_passed
print(f"{student1.name} - Passed: {student1.is_passed()}")
print(f"{student2.name} - Passed: {student2.is_passed()}")
