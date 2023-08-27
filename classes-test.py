class Student:

    def __init__(self,name, year, start_time, end_time):
        self.name = name
        self.year = year
        self.grades = []
    
    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)

    def display(self):
        print(self.year)

    def __repr__(self):
        return self.name
    
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:    
    minimum_passing = 65
    
    def __init__(self,score):
        self.score = score
    
pieter_Grade = Grade(100)
pieter.add_grade(pieter_Grade)
#pieter.display()

print(pieter)

 