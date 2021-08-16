"""
Write a program that takes in one parameter, an integer, that lies between 1 and 7
and print the day of the week as follows:
If the user enters:
1, the output should be Monday
2, the output should be Tuesday
3, the output should be Wednesday
4, The output should be Thursday
5, The output should be Friday
6, The output should be Saturday
7, The output should be Sunday
- Note: The integer should lie between 1 and 7 and should prompt the User to enter a valid
 value if any other value is entered

 - We have to ensure that the number the user enters is an integer
"""


# Type conversion
# int(data), float(data), bool(), str()
# Check for the datatype = type(data)
# Modules == Rewritting code
def check_day(day_of_the_week):
    if day_of_the_week == "1" or day_of_the_week == "1.0":
        print("Monday")
    elif day_of_the_week == "2" or day_of_the_week == "2.0":
        print("Tuesday")
    elif day_of_the_week == "3" or day_of_the_week == "3.0":
        print("Wednesday")
    elif day_of_the_week == "4" or day_of_the_week == "4.0":
        print("Thursday")
    elif day_of_the_week == "5" or day_of_the_week == "5.0":
        print("Friday")
    elif day_of_the_week == "6" or day_of_the_week == "6.0":
        print("Saturday")
    elif day_of_the_week == "7" or day_of_the_week == "7.0":
        print("Sunday")
    else:
        print("Invalid value. Please check that you have entered a valid value")


x = input("Enter an integer between 1 and 7: ")
check_day(x)  # Calling the function
