marks = int(input("Enter the marks: "))


def check_passed_or_failed():
    if marks < 40:
        print("The student has failed")
    else:
        print("The student has passed")


# Naming functions follows all the variable naming rules
# noinspection PyChainedComparisons
def check_grade():
    if marks <= 30:
        print("The student has scored an F")
    elif marks > 30 and marks <= 40:
        print("The student has scored a D")
    elif marks > 40 and marks <= 50:
        print("The student score a C")
    elif marks > 50 and marks <= 60:
        print("The student scored a B")
    else:
        print("The student scored and A")


check_grade()
check_passed_or_failed()
