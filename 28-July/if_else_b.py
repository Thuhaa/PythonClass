marks = int(input("Enter the marks: ")) # Enter the marks

# Between 0 and 30 == F
# Between 31 and 40 == D
# Between 41 and 50 == C
# Between 51 and 60 == B
# Above 61 == A
# True and True == True
# True and False == False
# False and False == False
# True or True == True
# True or False == True
# False and False == False
# Use elif If there is more than 2 condition

if marks <= 30:
    print("The student has scored an F")
elif marks > 30 and marks <=40:
    print("The student has scored a D")
elif marks >40 and marks<=50:
    print("The student score a C")
elif marks > 50 and marks <= 60:
    print("The student scored a B")
else:
    print("The student scored and A")





