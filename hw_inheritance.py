"""
                    Collage
                    Faculty
    Teacher                         Student
Period  Salary              Subject.   Mark.(excellent=90%,Good=80%)   Fee.
"""
from __future__ import print_function

class College:
    def __init__(self,name):
        self.collegeName = name
class Faculty(College):
    def __init__(self,c_name,faculty):
        College.__init__(self,c_name)
        self.faculty = faculty
    def print_info(self):
        print("Collage:",self.name,"\t\tFaculty:",self.faculty)
class Teacher(Faculty):
    def __init__(self,c_name,name,faculty,no_Of_period,salary):
        Faculty.__init__(self,c_name,faculty)
        self.name = name
        self.no_Of_period = no_Of_period
        self.salary = salary
    def print_info(self):
        Faculty.print_info(self)
        print("The",self.faculty,"named",self.name,"teaches for",self.no_Of_period,"periods and has a salary of Rs.",self.salary)
class Student(Faculty):
    def __init__(self,c_name,name,faculty,no_of_subject,mark,fee):
        Faculty.__init__(self,c_name,faculty)
        self.name = name
        self.no_of_subject = no_of_subject
        self.mark = mark
        self.fee = fee
    def print_info(self):
        Faculty.print_info(self)
        print("The",self.faculty,"named",self.name,"studies",self.no_of_subject,"subjects and pays a monthly fee Rs.",self.fee)
        self.marks_evaluation()
    def marks_evaluation(self):
        for m in self.mark:
            print(self.name,"is",end=" ")
            if self.mark[m] >=90:
                print("excellent in %s."%m)
            elif self.mark[m] >=80:
                print("very good in %s."%m)
            elif self.mark[m] >=70:
                print("good in %s."%m)
            else:
                print("satisfactory in %s."%m)

teacher = Teacher("SIA College","Asmin","teacher",5,30000)
student = Student("Bernhardt Collage","Abisha","student",8,{"math": 100,"english": 80,"nepali":60},8000)
teacher.print_info()
print("\n")
student.print_info()