# Assume a student
# Class Students
# Faculty
# name, reg, fees_payment
# __init__ # Initialize method, ca
# C language + C++
# GDAL = Geospatial Data Abstraction Library == C++

class Student:
    def __init__(self, name, reg, fees):
        self.name = name
        self.reg = reg
        self.fees = fees

    def student_details(self):
        return "".join(f"{self.name} Reg No:{self.reg} has paid:{self.fees}")


student1 = Student("Moffat", "ESSQ", 20000)
student2 = Student("Caleb", "ESSQ", 40000)

print(student1.student_details())
