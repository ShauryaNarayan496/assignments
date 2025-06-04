class Student:
    def __init__(self, name, age, marks):
        self.name = name 
        self.age = age 
        self.marks = marks 
    def calculate_gpa(self):
        return ((marks/100)*4)

    